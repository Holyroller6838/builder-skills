from __future__ import annotations

from ..models import (
    CommandFailed,
    CommandMissing,
    CommandOk,
    CommandOutcome,
    NormalizedHostData,
    NormalizedPairData,
)
from .collectors import RawCommandEntry
from .parsers import (
    ParseError,
    parse_show_bgp_summary,
    parse_show_interfaces_status,
    parse_show_mlag,
    parse_show_version,
)

# Our own mapping from check name to the canonical command it depends on —
# not a mapping of any invented Itential/EOS schema, just which of the four
# confirmed commands each check needs.
CANONICAL_COMMAND_FOR_CHECK: dict[str, str] = {
    "version": "show version",
    "mlag": "show mlag",
    "bgp": "show ip bgp summary",
    "interfaces": "show interfaces status",
}

PARSER_FOR_CHECK = {
    "version": parse_show_version,
    "mlag": parse_show_mlag,
    "bgp": parse_show_bgp_summary,
    "interfaces": parse_show_interfaces_status,
}


def _normalize_check(commands: dict[str, RawCommandEntry], check_name: str) -> CommandOutcome:
    canonical_command = CANONICAL_COMMAND_FOR_CHECK[check_name]
    entry = commands.get(canonical_command)
    if entry is None:
        return CommandMissing()
    if not entry.success:
        return CommandFailed(f"{canonical_command} reported success=false")

    parser = PARSER_FOR_CHECK[check_name]
    try:
        parsed = parser(entry.output)
    except NotImplementedError as exc:
        return CommandFailed(f"{canonical_command} parser not yet implemented: {exc}")
    except ParseError as exc:
        return CommandFailed(f"could not parse {canonical_command} output: {exc}")
    return CommandOk(parsed)


def _normalize_host(
    commands: dict[str, RawCommandEntry], hostname: str, required_checks: frozenset[str]
) -> NormalizedHostData:
    return NormalizedHostData(
        hostname=hostname,
        version=_normalize_check(commands, "version"),
        mlag=_normalize_check(commands, "mlag") if "mlag" in required_checks else CommandMissing(),
        bgp=_normalize_check(commands, "bgp") if "bgp" in required_checks else CommandMissing(),
        interfaces=_normalize_check(commands, "interfaces"),
    )


def normalize_pair_data(
    grouped: dict[str, dict[str, RawCommandEntry]],
    device_a_hostname: str,
    device_b_hostname: str,
    required_checks: frozenset[str],
) -> NormalizedPairData:
    return NormalizedPairData(
        device_a=_normalize_host(grouped.get(device_a_hostname, {}), device_a_hostname, required_checks),
        device_b=_normalize_host(grouped.get(device_b_hostname, {}), device_b_hostname, required_checks),
    )
