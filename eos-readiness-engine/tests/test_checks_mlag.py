from eos_readiness.checks import check_mlag
from eos_readiness.models import CommandFailed, CommandMissing
from eos_readiness.status import Status
from tests.factories import make_host, make_pair, ok_mlag


def test_both_active_passes():
    result = check_mlag(make_pair())
    assert result.status == Status.PASS


def test_disabled_on_one_host_fails():
    host_a = make_host("A", mlag=ok_mlag("disabled"))
    result = check_mlag(make_pair(host_a=host_a))
    assert result.status == Status.FAIL
    assert any("disabled on A" in r for r in result.reasons)


def test_disabled_on_both_hosts_fails_with_both_reasons():
    host_a = make_host("A", mlag=ok_mlag("disabled"))
    host_b = make_host("B", mlag=ok_mlag("disabled"))
    result = check_mlag(make_pair(host_a=host_a, host_b=host_b))
    assert result.status == Status.FAIL
    assert len(result.reasons) == 2


def test_hosts_disagree_on_state_warns():
    host_a = make_host("A", mlag=ok_mlag("active"))
    host_b = make_host("B", mlag=ok_mlag("standby"))
    result = check_mlag(make_pair(host_a=host_a, host_b=host_b))
    assert result.status == Status.WARNING


def test_both_hosts_report_same_ambiguous_state_warns():
    host_a = make_host("A", mlag=ok_mlag("unknown"))
    host_b = make_host("B", mlag=ok_mlag("unknown"))
    result = check_mlag(make_pair(host_a=host_a, host_b=host_b))
    assert result.status == Status.WARNING


def test_command_failed_fails():
    host_a = make_host("A", mlag=CommandFailed("no route to host"))
    result = check_mlag(make_pair(host_a=host_a))
    assert result.status == Status.FAIL


def test_command_missing_fails():
    host_b = make_host("B", mlag=CommandMissing())
    result = check_mlag(make_pair(host_b=host_b))
    assert result.status == Status.FAIL
