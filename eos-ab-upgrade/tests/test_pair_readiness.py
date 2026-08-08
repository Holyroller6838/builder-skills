"""Unit tests for eos_ab_upgrade.pair_readiness."""

from __future__ import annotations

from copy import deepcopy

from eos_ab_upgrade.pair_readiness import evaluate_pair_readiness


def _healthy_side(device_name: str) -> dict:
    return {
        "device_name": device_name,
        "reachable": True,
        "version": "4.29.2F",
        "mlag_state": "active",
        "mlag_peer_state": "connected",
        "bgp_established": 8,
        "bgp_expected": 8,
        "critical_interfaces_up": 4,
        "critical_interfaces_expected": 4,
    }


def _healthy_policy() -> dict:
    return {
        "supported_source_versions": ["4.28", "4.29", "4.30", "4.31"],
        "require_mlag_active": True,
        "minimum_bgp_health_percent": 100,
        "minimum_interface_health_percent": 100,
    }


def _healthy_pair() -> dict:
    return {
        "side_a": _healthy_side("leaf-a"),
        "side_b": _healthy_side("leaf-b"),
        "policy": _healthy_policy(),
    }


def test_healthy_pair_is_eligible():
    result = evaluate_pair_readiness(_healthy_pair())

    assert result["eligible"] is True
    assert result["blocking_reasons"] == []
    assert result["warnings"] == []
    assert result["baseline"]["pair_health"] == "healthy"
    assert result["baseline"]["side_a"]["bgp_health_percent"] == 100.0
    assert result["baseline"]["side_a"]["interface_health_percent"] == 100.0
    assert result["baseline"]["side_b"]["status"] == "healthy"


def test_side_a_unreachable_is_blocking():
    data = _healthy_pair()
    data["side_a"]["reachable"] = False

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is False
    assert result["baseline"]["pair_health"] == "failed"
    assert any("side_a" in reason and "unreachable" in reason for reason in result["blocking_reasons"])


def test_side_b_unreachable_is_blocking():
    data = _healthy_pair()
    data["side_b"]["reachable"] = False

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is False
    assert result["baseline"]["pair_health"] == "failed"
    assert any("side_b" in reason and "unreachable" in reason for reason in result["blocking_reasons"])


def test_unsupported_eos_version_is_blocking():
    data = _healthy_pair()
    data["side_a"]["version"] = "4.27.0F"

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is False
    assert result["baseline"]["pair_health"] == "failed"
    assert any("unsupported EOS version" in reason for reason in result["blocking_reasons"])
    assert result["baseline"]["side_a"]["version_supported"] is False


def test_mlag_inactive_is_blocking():
    data = _healthy_pair()
    data["side_a"]["mlag_state"] = "inactive"

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is False
    assert result["baseline"]["pair_health"] == "degraded"
    assert any("unhealthy MLAG state" in reason for reason in result["blocking_reasons"])


def test_mlag_peer_disconnected_is_blocking():
    data = _healthy_pair()
    data["side_b"]["mlag_peer_state"] = "disconnected"

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is False
    assert result["baseline"]["pair_health"] == "degraded"
    assert any("unhealthy MLAG peer state" in reason for reason in result["blocking_reasons"])


def test_bgp_below_threshold_is_blocking():
    data = _healthy_pair()
    data["policy"]["minimum_bgp_health_percent"] = 90
    # 6/8 = 75% — calculated, not hardcoded as a count check
    data["side_a"]["bgp_established"] = 6
    data["side_a"]["bgp_expected"] = 8

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is False
    assert result["baseline"]["side_a"]["bgp_health_percent"] == 75.0
    assert any("BGP health" in reason and "below policy threshold" in reason for reason in result["blocking_reasons"])


def test_critical_interfaces_below_threshold_is_blocking():
    data = _healthy_pair()
    data["policy"]["minimum_interface_health_percent"] = 100
    # 3/4 = 75%
    data["side_b"]["critical_interfaces_up"] = 3
    data["side_b"]["critical_interfaces_expected"] = 4

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is False
    assert result["baseline"]["side_b"]["interface_health_percent"] == 75.0
    assert any(
        "critical interface health" in reason and "below policy threshold" in reason
        for reason in result["blocking_reasons"]
    )


def test_missing_required_input_is_blocking():
    data = _healthy_pair()
    del data["side_a"]["bgp_expected"]
    del data["policy"]["minimum_bgp_health_percent"]

    # Missing side field
    side_result = evaluate_pair_readiness(
        {
            "side_a": data["side_a"],
            "side_b": _healthy_side("leaf-b"),
            "policy": _healthy_policy(),
        }
    )
    assert side_result["eligible"] is False
    assert side_result["baseline"]["pair_health"] == "failed"
    assert any("missing required data" in reason and "bgp_expected" in reason for reason in side_result["blocking_reasons"])

    # Missing top-level section
    top_result = evaluate_pair_readiness({"side_a": _healthy_side("leaf-a")})
    assert top_result["eligible"] is False
    assert any("missing required data: 'side_b'" in reason for reason in top_result["blocking_reasons"])
    assert any("missing required data: 'policy'" in reason for reason in top_result["blocking_reasons"])


def test_both_sides_degraded():
    data = _healthy_pair()
    data["policy"]["minimum_bgp_health_percent"] = 100
    data["policy"]["minimum_interface_health_percent"] = 100
    # Both sides below threshold via calculated percentages
    data["side_a"]["bgp_established"] = 7
    data["side_a"]["bgp_expected"] = 8  # 87.5%
    data["side_b"]["critical_interfaces_up"] = 2
    data["side_b"]["critical_interfaces_expected"] = 4  # 50%

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is False
    assert result["baseline"]["pair_health"] == "degraded"
    assert result["baseline"]["side_a"]["status"] == "degraded"
    assert result["baseline"]["side_b"]["status"] == "degraded"
    assert result["baseline"]["side_a"]["bgp_health_percent"] == 87.5
    assert result["baseline"]["side_b"]["interface_health_percent"] == 50.0
    assert len(result["blocking_reasons"]) >= 2


def test_partial_health_above_threshold_emits_warning_not_block():
    """Imperfect but policy-compliant health should warn and mark degraded, not block."""
    data = _healthy_pair()
    data["policy"]["minimum_bgp_health_percent"] = 80
    data["policy"]["minimum_interface_health_percent"] = 80
    data["side_a"]["bgp_established"] = 9
    data["side_a"]["bgp_expected"] = 10  # 90%

    result = evaluate_pair_readiness(data)

    assert result["eligible"] is True
    assert result["blocking_reasons"] == []
    assert result["baseline"]["pair_health"] == "degraded"
    assert result["baseline"]["side_a"]["bgp_health_percent"] == 90.0
    assert any("BGP health" in warning for warning in result["warnings"])


def test_does_not_hardcode_hostnames_or_versions():
    """Policy and side names come from input — no baked-in inventory assumptions."""
    data = {
        "side_a": _healthy_side("custom-spine-west-01"),
        "side_b": _healthy_side("custom-spine-west-02"),
        "policy": {
            "supported_source_versions": ["4.32"],
            "require_mlag_active": True,
            "minimum_bgp_health_percent": 50,
            "minimum_interface_health_percent": 50,
        },
    }
    data["side_a"]["version"] = "4.32.1M"
    data["side_b"]["version"] = "4.32.1M"
    data["side_a"]["bgp_established"] = 1
    data["side_a"]["bgp_expected"] = 2
    data["side_b"]["bgp_established"] = 1
    data["side_b"]["bgp_expected"] = 2

    result = evaluate_pair_readiness(deepcopy(data))

    assert result["eligible"] is True
    assert result["baseline"]["side_a"]["device_name"] == "custom-spine-west-01"
    assert result["baseline"]["side_b"]["device_name"] == "custom-spine-west-02"
    assert result["baseline"]["side_a"]["bgp_health_percent"] == 50.0
