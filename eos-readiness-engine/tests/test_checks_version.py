from eos_readiness.checks import check_version
from eos_readiness.models import CommandFailed, CommandMissing
from eos_readiness.status import Status
from tests.factories import make_host, make_pair, ok_version


def test_matching_version_passes():
    result = check_version(make_pair(), "4.33.1F")
    assert result.status == Status.PASS


def test_mismatched_version_fails():
    result = check_version(make_pair(), "4.30.0F")
    assert result.status == Status.FAIL
    assert any("expected '4.30.0F'" in r for r in result.reasons)


def test_no_target_version_configured_warns():
    result = check_version(make_pair(), None)
    assert result.status == Status.WARNING


def test_command_failed_fails_regardless_of_target_version():
    host_a = make_host("A", version=CommandFailed("boom"))
    result = check_version(make_pair(host_a=host_a), None)
    assert result.status == Status.FAIL


def test_command_missing_fails():
    host_b = make_host("B", version=CommandMissing())
    result = check_version(make_pair(host_b=host_b), "4.33.1F")
    assert result.status == Status.FAIL


def test_one_host_mismatched_reports_only_that_host():
    host_a = make_host("A", version=ok_version("4.20.0F"))
    result = check_version(make_pair(host_a=host_a), "4.33.1F")
    assert result.status == Status.FAIL
    assert any("A" in r for r in result.reasons)
    assert not any("USILD001LAB01B" in r for r in result.reasons)
