from __future__ import annotations

from dataclasses import dataclass

from ..errors import ProfileNotFoundError

BASE_CHECKS: frozenset[str] = frozenset({"collection", "version", "interfaces"})


@dataclass(frozen=True)
class ProfileConfig:
    name: str
    checks_enabled: frozenset[str]


PROFILES: dict[str, ProfileConfig] = {
    "mlag_bgp": ProfileConfig("mlag_bgp", BASE_CHECKS | {"mlag", "bgp"}),
    "bgp_only": ProfileConfig("bgp_only", BASE_CHECKS | {"bgp"}),
    "mlag_only": ProfileConfig("mlag_only", BASE_CHECKS | {"mlag"}),
    "basic_pair": ProfileConfig("basic_pair", BASE_CHECKS),
}


def resolve_profile(name: str) -> ProfileConfig:
    profile = PROFILES.get(name)
    if profile is None:
        raise ProfileNotFoundError(name)
    return profile
