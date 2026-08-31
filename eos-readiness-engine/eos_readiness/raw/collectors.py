from __future__ import annotations

from dataclasses import dataclass

# Recognized command aliases seen in real Itential GatewayManager sendCommand
# output. Only "sh mlag" is confirmed as an alias of "show mlag" — no other
# aliases are invented here.
COMMAND_ALIASES: dict[str, str] = {
    "sh mlag": "show mlag",
}


def canonicalize_command(command: str) -> str:
    stripped = command.strip()
    return COMMAND_ALIASES.get(stripped, stripped)


@dataclass(frozen=True)
class RawCommandEntry:
    output: str
    success: bool


def group_by_device_and_command(command_results: list[dict]) -> dict[str, dict[str, RawCommandEntry]]:
    # command_results is the verified live GatewayManager sendCommand
    # result.result.results[] array, unmodified — each item carries
    # command/host/name/output/success (plus elapsed_time/start_time/end_time,
    # which this layer never reads).
    grouped: dict[str, dict[str, RawCommandEntry]] = {}
    for item in command_results:
        hostname = item["name"]
        canonical = canonicalize_command(item["command"])
        grouped.setdefault(hostname, {})[canonical] = RawCommandEntry(
            output=item["output"],
            success=item["success"],
        )
    return grouped
