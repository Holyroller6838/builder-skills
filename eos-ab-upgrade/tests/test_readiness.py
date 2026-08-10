import pytest

from services.eos_upgrade import readiness
from services.eos_upgrade.models import Device
from tests.fixtures.readiness_payloads import (
    BGP_SUMMARY_SAMPLE,
    CONNECTIVITY_DOWN,
    CONNECTIVITY_UP,
    FACTS_SUPPORTED_VERSION,
    FACTS_UNSUPPORTED_VERSION,
    INTERFACES_CLEAN,
    INTERFACES_DEGRADED,
    MLAG_HEALTHY,
    MLAG_UNHEALTHY,
    PASSING_PAYLOAD,
    payload_with,
)


def make_device() -> Device:
    return Device(hostname="lab-leaf-a", management_ip="10.10.10.1", adapter_id="arista-eos-lab")


def test_check_reachable_true():
    assert readiness.check_reachable(CONNECTIVITY_UP) is True


def test_check_reachable_false():
    assert readiness.check_reachable(CONNECTIVITY_DOWN) is False


def test_check_source_version_supported_true():
    assert readiness.check_source_version_supported(FACTS_SUPPORTED_VERSION) is True


def test_check_source_version_supported_false():
    assert readiness.check_source_version_supported(FACTS_UNSUPPORTED_VERSION) is False


def test_check_mlag_healthy_true():
    assert readiness.check_mlag_healthy(MLAG_HEALTHY) is True


def test_check_mlag_healthy_false():
    assert readiness.check_mlag_healthy(MLAG_UNHEALTHY) is False


def test_check_interfaces_healthy_true():
    assert readiness.check_interfaces_healthy(INTERFACES_CLEAN) is True


def test_check_interfaces_healthy_false():
    assert readiness.check_interfaces_healthy(INTERFACES_DEGRADED) is False


def test_evaluate_readiness_passes_when_all_checks_clear():
    device = make_device()

    passed, details = readiness.evaluate_readiness(
        device, "4.31.1", CONNECTIVITY_UP, FACTS_SUPPORTED_VERSION, MLAG_HEALTHY, INTERFACES_CLEAN
    )

    assert passed is True
    assert details == {
        "reachable": True,
        "source_version_supported": True,
        "mlag_healthy": True,
        "interfaces_healthy": True,
    }


def test_evaluate_readiness_fails_closed_on_single_bad_check():
    device = make_device()

    passed, details = readiness.evaluate_readiness(
        device, "4.31.1", CONNECTIVITY_UP, FACTS_SUPPORTED_VERSION, MLAG_UNHEALTHY, INTERFACES_CLEAN
    )

    assert passed is False
    assert details["mlag_healthy"] is False


def test_build_readiness_evidence_shape():
    device = make_device()

    evidence = readiness.build_readiness_evidence(
        device, "4.31.1", True, {"reachable": True}, BGP_SUMMARY_SAMPLE
    )

    assert evidence["device_hostname"] == "lab-leaf-a"
    assert evidence["target_version"] == "4.31.1"
    assert evidence["passed"] is True
    assert evidence["details"] == {"reachable": True}
    assert evidence["bgp_summary"] == BGP_SUMMARY_SAMPLE
    assert "generated_at" in evidence


def test_run_readiness_check_from_payload_happy_path():
    evidence = readiness.run_readiness_check_from_payload(PASSING_PAYLOAD)

    assert evidence["passed"] is True
    assert evidence["device_hostname"] == "lab-leaf-a"
    assert evidence["bgp_summary"] == BGP_SUMMARY_SAMPLE


def test_run_readiness_check_from_payload_reports_failure_without_raising():
    payload = payload_with(interfaces=INTERFACES_DEGRADED)

    evidence = readiness.run_readiness_check_from_payload(payload)

    assert evidence["passed"] is False
    assert evidence["details"]["interfaces_healthy"] is False


def test_run_readiness_check_from_payload_raises_on_missing_top_level_key():
    payload = payload_with()
    del payload["mlag_status"]

    with pytest.raises(ValueError, match="mlag_status"):
        readiness.run_readiness_check_from_payload(payload)
