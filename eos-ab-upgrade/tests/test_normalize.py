"""Tests for eos_ab_upgrade.normalize — LAB01A-style CVP and MVP1 side mapping."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from eos_ab_upgrade.normalize import normalize_pair_readiness, normalize_side
from eos_ab_upgrade.pair_readiness import evaluate_pair_readiness

FIXTURES = Path(__file__).parent / "fixtures"


def _load(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


def test_normalize_lab01a_cvp_device_verifies_identity_reachability_version():
    device = _load("lab01a_cvp_device.json")
    side = normalize_side(device)

    assert side["device_name"] == "LAB01A"
    assert side["reachable"] is True
    assert side["version"] == "4.29.2F"
    assert side["field_status"]["identity"] == "verified"
    assert side["field_status"]["reachability"] == "verified"
    assert side["field_status"]["version"] == "verified"


def test_normalize_lab01a_cvp_marks_mlag_bgp_interfaces_unverified():
    """CVP inventory has no show mlag / bgp / interfaces — must stay unverified."""
    side = normalize_side(_load("lab01a_cvp_device.json"))

    assert side["mlag_state"] is None
    assert side["mlag_peer_state"] is None
    assert side["bgp_established"] is None
    assert side["bgp_expected"] is None
    assert side["critical_interfaces_up"] is None
    assert side["critical_interfaces_expected"] is None
    assert side["field_status"]["mlag"] == "unverified"
    assert side["field_status"]["bgp"] == "unverified"
    assert side["field_status"]["interfaces"] == "unverified"


def test_normalize_lab01_cvp_pair_and_evaluate_skips_unverified_ops():
    raw = _load("lab01_cvp_pair.json")
    canonical = normalize_pair_readiness(raw)

    assert canonical["side_a"]["device_name"] == "LAB01A"
    assert canonical["side_b"]["device_name"] == "LAB01B"
    for side_key in ("side_a", "side_b"):
        status = canonical[side_key]["field_status"]
        assert status["mlag"] == "unverified"
        assert status["bgp"] == "unverified"
        assert status["interfaces"] == "unverified"

    result = evaluate_pair_readiness(canonical)

    assert result["eligible"] is True
    assert result["baseline"]["pair_health"] == "healthy"
    assert any("mlag fields are unverified" in w for w in result["warnings"])
    assert any("bgp fields are unverified" in w for w in result["warnings"])
    assert any("interfaces fields are unverified" in w for w in result["warnings"])
    assert result["baseline"]["side_a"]["bgp_health_percent"] is None
    assert result["baseline"]["side_a"]["interface_health_percent"] is None


def test_normalize_cvp_inactive_streaming_is_unreachable():
    device = _load("lab01a_cvp_device.json")
    device["streamingStatus"] = "inactive"
    side = normalize_side(device)
    assert side["reachable"] is False

    pair = {
        "side_a": device,
        "side_b": _load("lab01b_cvp_device.json"),
        "policy": {
            "supported_source_versions": ["4.28", "4.29", "4.30", "4.31"],
            "require_mlag_active": True,
            "minimum_bgp_health_percent": 100,
            "minimum_interface_health_percent": 100,
        },
    }
    result = evaluate_pair_readiness(normalize_pair_readiness(pair))
    assert result["eligible"] is False
    assert any("unreachable" in r for r in result["blocking_reasons"])


def test_normalize_mvp1_side_does_not_treat_peer_state_as_verified_mlag():
    """Invented peer_state.healthy is not a live operational-command capture."""
    side = normalize_side(
        {
            "hostname": "leaf-a",
            "management_ip": "10.0.0.1",
            "adapter_id": "eos-adapter",
            "facts": {
                "version": "4.31.1",
                "interface_capacity_headroom_pct": 100,
                "interfaces_down": 0,
            },
            "peer_state": {"healthy": True},
        }
    )
    assert side["device_name"] == "leaf-a"
    assert side["version"] == "4.31.1"
    assert side["reachable"] is True
    assert side["field_status"]["mlag"] == "unverified"
    assert side["mlag_state"] is None
    assert side["field_status"]["bgp"] == "unverified"
    assert side["field_status"]["interfaces"] == "unverified"


def test_normalize_mvp1_pair_envelope():
    payload = {
        "pair_id": "lab-pair-01",
        "target_version": "4.31.1",
        "side_a": {
            "hostname": "leaf-a",
            "management_ip": "10.0.0.1",
            "adapter_id": "eos",
            "facts": {"version": "4.29.2F"},
            "peer_state": {"healthy": True},
        },
        "side_b": {
            "hostname": "leaf-b",
            "management_ip": "10.0.0.2",
            "adapter_id": "eos",
            "facts": {"version": "4.29.2F"},
            "peer_state": {"healthy": True},
        },
    }
    canonical = normalize_pair_readiness(payload)
    assert canonical["side_a"]["device_name"] == "leaf-a"
    assert canonical["side_b"]["device_name"] == "leaf-b"
    assert "supported_source_versions" in canonical["policy"]


def test_normalize_rejects_unknown_side_shape():
    with pytest.raises(ValueError, match="unrecognized side record"):
        normalize_side({"foo": "bar"})


def test_canonical_passthrough_preserves_verified_operational_fields():
    canonical = {
        "side_a": {
            "device_name": "leaf-a",
            "reachable": True,
            "version": "4.29.2F",
            "mlag_state": "active",
            "mlag_peer_state": "connected",
            "bgp_established": 8,
            "bgp_expected": 8,
            "critical_interfaces_up": 4,
            "critical_interfaces_expected": 4,
            "field_status": {
                "identity": "verified",
                "reachability": "verified",
                "version": "verified",
                "mlag": "verified",
                "bgp": "verified",
                "interfaces": "verified",
            },
        },
        "side_b": {
            "device_name": "leaf-b",
            "reachable": True,
            "version": "4.29.2F",
            "mlag_state": "active",
            "mlag_peer_state": "connected",
            "bgp_established": 8,
            "bgp_expected": 8,
            "critical_interfaces_up": 4,
            "critical_interfaces_expected": 4,
            "field_status": {
                "identity": "verified",
                "reachability": "verified",
                "version": "verified",
                "mlag": "verified",
                "bgp": "verified",
                "interfaces": "verified",
            },
        },
        "policy": {
            "supported_source_versions": ["4.28", "4.29", "4.30", "4.31"],
            "require_mlag_active": True,
            "minimum_bgp_health_percent": 100,
            "minimum_interface_health_percent": 100,
        },
    }
    out = normalize_pair_readiness(canonical)
    assert out["side_a"]["mlag_state"] == "active"
    assert out["side_a"]["field_status"]["mlag"] == "verified"
    result = evaluate_pair_readiness(out)
    assert result["eligible"] is True
    assert result["warnings"] == []
