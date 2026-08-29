from eos_readiness.checks import check_interfaces
from eos_readiness.models import CommandFailed, CommandMissing
from eos_readiness.status import Status
from tests.factories import make_host, make_pair, ok_interfaces


def test_all_critical_interfaces_up_passes():
    critical = {"USILD001LAB01A": ["Ethernet1"], "USILD001LAB01B": ["Ethernet1"]}
    result = check_interfaces(make_pair(), critical)
    assert result.status == Status.PASS


def test_critical_interface_down_fails():
    host_a = make_host("A", interfaces=ok_interfaces([("Ethernet1", False)]))
    result = check_interfaces(make_pair(host_a=host_a), {"A": ["Ethernet1"]})
    assert result.status == Status.FAIL


def test_critical_interface_not_found_fails():
    host_a = make_host("A", interfaces=ok_interfaces([("Ethernet9", True)]))
    result = check_interfaces(make_pair(host_a=host_a), {"A": ["Ethernet1"]})
    assert result.status == Status.FAIL
    assert any("not found on A" in r for r in result.reasons)


def test_no_critical_list_configured_warns():
    result = check_interfaces(make_pair(), {})
    assert result.status == Status.WARNING


def test_no_critical_list_surfaces_down_interfaces_as_reasons():
    host_a = make_host("A", interfaces=ok_interfaces([("Ethernet1", False)]))
    result = check_interfaces(make_pair(host_a=host_a), {})
    assert result.status == Status.WARNING
    assert any("Ethernet1" in r for r in result.reasons)


def test_zero_interfaces_reported_fails():
    host_a = make_host("A", interfaces=ok_interfaces([]))
    result = check_interfaces(make_pair(host_a=host_a), {})
    assert result.status == Status.FAIL


def test_empty_critical_list_is_vacuously_pass():
    critical = {"USILD001LAB01A": [], "USILD001LAB01B": []}
    result = check_interfaces(make_pair(), critical)
    assert result.status == Status.PASS


def test_command_failed_fails():
    host_a = make_host("A", interfaces=CommandFailed("timeout"))
    result = check_interfaces(make_pair(host_a=host_a), {})
    assert result.status == Status.FAIL


def test_command_missing_fails():
    host_b = make_host("B", interfaces=CommandMissing())
    result = check_interfaces(make_pair(host_b=host_b), {})
    assert result.status == Status.FAIL
