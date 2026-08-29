from eos_readiness.checks import check_collection
from eos_readiness.models import CommandFailed, CommandMissing
from eos_readiness.status import Status
from tests.factories import make_host, make_pair

FULL = frozenset({"collection", "version", "interfaces", "mlag", "bgp"})
BASIC = frozenset({"collection", "version", "interfaces"})


def test_all_healthy_passes():
    result = check_collection(make_pair(), FULL)
    assert result.status == Status.PASS
    assert result.reasons == []


def test_version_failed_fails_collection():
    host_a = make_host("A", version=CommandFailed("timeout"))
    result = check_collection(make_pair(host_a=host_a), FULL)
    assert result.status == Status.FAIL
    assert any("version failed on A" in r for r in result.reasons)


def test_interfaces_missing_fails_collection():
    host_b = make_host("B", interfaces=CommandMissing())
    result = check_collection(make_pair(host_b=host_b), FULL)
    assert result.status == Status.FAIL
    assert any("interfaces data missing on B" in r for r in result.reasons)


def test_mlag_failure_ignored_when_profile_does_not_require_mlag():
    host_a = make_host("A", mlag=CommandFailed("no such command"))
    result = check_collection(make_pair(host_a=host_a), BASIC)
    assert result.status == Status.PASS


def test_mlag_failure_fails_collection_when_profile_requires_mlag():
    host_a = make_host("A", mlag=CommandFailed("no such command"))
    result = check_collection(make_pair(host_a=host_a), BASIC | {"mlag"})
    assert result.status == Status.FAIL


def test_bgp_missing_ignored_when_profile_does_not_require_bgp():
    host_b = make_host("B", bgp=CommandMissing())
    result = check_collection(make_pair(host_b=host_b), BASIC | {"mlag"})
    assert result.status == Status.PASS


def test_bgp_missing_fails_when_profile_requires_bgp():
    host_b = make_host("B", bgp=CommandMissing())
    result = check_collection(make_pair(host_b=host_b), BASIC | {"bgp"})
    assert result.status == Status.FAIL
