from __future__ import annotations

from ..models import BgpFacts, InterfacesFacts, MlagFacts, VersionFacts

# These parsers operate only on a single command's raw CLI output string.
# They know nothing about Itential, GatewayManager, or CVP — that boundary
# lives in raw/collectors.py and raw/normalize.py.

VERSION_LABEL = "Software image version:"


class ParseError(Exception):
    pass


def parse_show_version(raw_output: str) -> VersionFacts:
    for line in raw_output.splitlines():
        stripped = line.strip()
        if stripped.startswith(VERSION_LABEL):
            value = stripped[len(VERSION_LABEL) :].strip()
            if value:
                return VersionFacts(version=value)
            break
    raise ParseError("could not find a 'Software image version:' line with a value")


def parse_show_mlag(raw_output: str) -> MlagFacts:
    # No real "sh mlag" / "show mlag" output has been captured from the lab
    # yet. Deliberately not implemented rather than guessed — see
    # eos-readiness-engine/README.md's Status section.
    raise NotImplementedError(
        "parse_show_mlag is not implemented — no real 'sh mlag'/'show mlag' output has been "
        "captured from the lab yet"
    )


def parse_show_bgp_summary(raw_output: str) -> BgpFacts:
    raise NotImplementedError(
        "parse_show_bgp_summary is not implemented — no real 'show ip bgp summary' output has "
        "been captured from the lab yet"
    )


def parse_show_interfaces_status(raw_output: str) -> InterfacesFacts:
    raise NotImplementedError(
        "parse_show_interfaces_status is not implemented — no real 'show interfaces status' "
        "output has been captured from the lab yet"
    )
