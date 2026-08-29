from eos_readiness.checks import check_bgp
from eos_readiness.models import CommandFailed, CommandMissing
from eos_readiness.status import Status
from tests.factories import make_host, make_pair, ok_bgp


def test_all_critical_peers_established_passes():
    critical = {"USILD001LAB01A": ["10.0.0.1"], "USILD001LAB01B": ["10.0.0.1"]}
    result = check_bgp(make_pair(), critical)
    assert result.status == Status.PASS


def test_critical_peer_not_established_fails():
    host_a = make_host("A", bgp=ok_bgp([("10.0.0.1", False)]))
    result = check_bgp(make_pair(host_a=host_a), {"A": ["10.0.0.1"]})
    assert result.status == Status.FAIL
    assert any("10.0.0.1" in r and "A" in r for r in result.reasons)


def test_critical_peer_not_found_fails():
    host_a = make_host("A", bgp=ok_bgp([("10.0.0.9", True)]))
    result = check_bgp(make_pair(host_a=host_a), {"A": ["10.0.0.1"]})
    assert result.status == Status.FAIL
    assert any("not found on A" in r for r in result.reasons)


def test_no_critical_list_configured_warns():
    result = check_bgp(make_pair(), {})
    assert result.status == Status.WARNING


def test_no_critical_list_surfaces_non_established_peers_as_reasons():
    host_a = make_host("A", bgp=ok_bgp([("10.0.0.1", False)]))
    result = check_bgp(make_pair(host_a=host_a), {})
    assert result.status == Status.WARNING
    assert any("10.0.0.1" in r for r in result.reasons)


def test_zero_peers_found_fails_even_without_critical_list():
    host_a = make_host("A", bgp=ok_bgp([]))
    result = check_bgp(make_pair(host_a=host_a), {})
    assert result.status == Status.FAIL
    assert any("no BGP peers found on A" in r for r in result.reasons)


def test_empty_critical_list_is_vacuously_pass_for_that_host():
    critical = {"USILD001LAB01A": [], "USILD001LAB01B": []}
    result = check_bgp(make_pair(), critical)
    assert result.status == Status.PASS


def test_command_failed_fails():
    host_a = make_host("A", bgp=CommandFailed("session reset"))
    result = check_bgp(make_pair(host_a=host_a), {})
    assert result.status == Status.FAIL


def test_command_missing_fails():
    host_b = make_host("B", bgp=CommandMissing())
    result = check_bgp(make_pair(host_b=host_b), {})
    assert result.status == Status.FAIL


def test_fail_on_one_host_beats_warning_on_the_other():
    host_a = make_host("A", bgp=ok_bgp([("10.0.0.1", False)]))
    host_b = make_host("B")
    result = check_bgp(make_pair(host_a=host_a, host_b=host_b), {"A": ["10.0.0.1"]})
    assert result.status == Status.FAIL
