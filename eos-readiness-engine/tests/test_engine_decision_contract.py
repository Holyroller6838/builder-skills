import json

import pytest

from eos_readiness.engine import evaluate_normalized
from eos_readiness.errors import ProfileNotFoundError
from tests.factories import make_host, make_pair, missing_host, ok_mlag, ok_version

FULL_CRITICAL_INTERFACES = {
    "USILD001LAB01A": ["Ethernet1"],
    "USILD001LAB01B": ["Ethernet1"],
}
FULL_CRITICAL_BGP = {
    "USILD001LAB01A": ["10.0.0.1"],
    "USILD001LAB01B": ["10.0.0.1"],
}


def test_mlag_bgp_all_pass_is_ready():
    result = evaluate_normalized(
        make_pair(),
        "mlag_bgp",
        target_version="4.33.1F",
        critical_interfaces=FULL_CRITICAL_INTERFACES,
        critical_bgp_peers=FULL_CRITICAL_BGP,
    )
    assert result["ready"] is True
    assert result["status"] == "PASS"
    assert result["checks"] == {
        "collection": "PASS",
        "version": "PASS",
        "mlag": "PASS",
        "bgp": "PASS",
        "interfaces": "PASS",
    }
    assert result["reasons"] == []
    assert result["pair"] == {"device_a": "USILD001LAB01A", "device_b": "USILD001LAB01B"}
    assert result["profile"] == "mlag_bgp"


def test_bgp_only_sets_mlag_not_applicable_and_stays_ready():
    result = evaluate_normalized(
        make_pair(),
        "bgp_only",
        target_version="4.33.1F",
        critical_interfaces=FULL_CRITICAL_INTERFACES,
        critical_bgp_peers=FULL_CRITICAL_BGP,
    )
    assert result["checks"]["mlag"] == "NOT_APPLICABLE"
    assert result["status"] == "PASS"
    assert result["ready"] is True


def test_mlag_only_sets_bgp_not_applicable_and_stays_ready():
    result = evaluate_normalized(
        make_pair(),
        "mlag_only",
        target_version="4.33.1F",
        critical_interfaces=FULL_CRITICAL_INTERFACES,
    )
    assert result["checks"]["bgp"] == "NOT_APPLICABLE"
    assert result["status"] == "PASS"
    assert result["ready"] is True


def test_basic_pair_sets_both_not_applicable_and_stays_ready():
    result = evaluate_normalized(
        make_pair(),
        "basic_pair",
        target_version="4.33.1F",
        critical_interfaces=FULL_CRITICAL_INTERFACES,
    )
    assert result["checks"]["mlag"] == "NOT_APPLICABLE"
    assert result["checks"]["bgp"] == "NOT_APPLICABLE"
    assert result["status"] == "PASS"
    assert result["ready"] is True


def test_not_applicable_never_causes_readiness_failure():
    # basic_pair evaluates neither mlag nor bgp — both NOT_APPLICABLE — and
    # that alone must never drag the pair out of PASS/ready.
    result = evaluate_normalized(
        make_pair(),
        "basic_pair",
        target_version="4.33.1F",
        critical_interfaces=FULL_CRITICAL_INTERFACES,
    )
    assert result["ready"] is True


def test_warning_status_results_in_ready_false():
    # No critical_interfaces/critical_bgp_peers supplied -> those checks WARN.
    result = evaluate_normalized(make_pair(), "mlag_bgp", target_version="4.33.1F")
    assert result["status"] == "WARNING"
    assert result["ready"] is False


def test_fail_beats_warning_in_overall_status():
    host_a = make_host("A", mlag=ok_mlag("disabled"))
    result = evaluate_normalized(make_pair(host_a=host_a), "mlag_bgp", target_version=None)
    assert result["status"] == "FAIL"
    assert result["ready"] is False


def test_reasons_aggregate_across_failing_checks():
    host_a = make_host("A", mlag=ok_mlag("disabled"), version=ok_version("4.10.0F"))
    result = evaluate_normalized(make_pair(host_a=host_a), "mlag_bgp", target_version="4.33.1F")
    assert result["status"] == "FAIL"
    assert len(result["reasons"]) >= 2


def test_unknown_profile_raises():
    with pytest.raises(ProfileNotFoundError):
        evaluate_normalized(make_pair(), "nonexistent_profile")


def test_completely_missing_host_data_fails_gracefully_not_an_exception():
    pair = make_pair(host_b=missing_host("USILD001LAB01B"))
    result = evaluate_normalized(pair, "mlag_bgp", target_version="4.33.1F")
    assert result["status"] == "FAIL"
    assert result["ready"] is False
    assert any("missing on USILD001LAB01B" in r for r in result["reasons"])


def test_output_is_json_serializable():
    result = evaluate_normalized(
        make_pair(),
        "mlag_bgp",
        target_version="4.33.1F",
        critical_interfaces=FULL_CRITICAL_INTERFACES,
        critical_bgp_peers=FULL_CRITICAL_BGP,
    )
    json.dumps(result)  # must not raise
