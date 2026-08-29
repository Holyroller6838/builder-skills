import pytest

from eos_readiness.errors import ProfileNotFoundError
from eos_readiness.profiles import BASE_CHECKS, PROFILES, resolve_profile


@pytest.mark.parametrize("name", ["mlag_bgp", "bgp_only", "mlag_only", "basic_pair"])
def test_every_profile_includes_base_checks(name):
    assert BASE_CHECKS <= PROFILES[name].checks_enabled


def test_mlag_bgp_enables_both_topology_checks():
    assert PROFILES["mlag_bgp"].checks_enabled == BASE_CHECKS | {"mlag", "bgp"}


def test_bgp_only_enables_bgp_not_mlag():
    checks = PROFILES["bgp_only"].checks_enabled
    assert "bgp" in checks
    assert "mlag" not in checks


def test_mlag_only_enables_mlag_not_bgp():
    checks = PROFILES["mlag_only"].checks_enabled
    assert "mlag" in checks
    assert "bgp" not in checks


def test_basic_pair_enables_neither_topology_check():
    checks = PROFILES["basic_pair"].checks_enabled
    assert "mlag" not in checks
    assert "bgp" not in checks


def test_resolve_profile_returns_config():
    assert resolve_profile("mlag_bgp") is PROFILES["mlag_bgp"]


def test_resolve_profile_raises_on_unknown_name():
    with pytest.raises(ProfileNotFoundError):
        resolve_profile("nonexistent_profile")
