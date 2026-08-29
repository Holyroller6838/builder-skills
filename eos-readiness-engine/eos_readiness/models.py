from __future__ import annotations

from dataclasses import dataclass, field

from .status import Status

# Everything below is OUR OWN normalized contract for what a check function
# consumes — not a mapping of any real EOS, CVP, Torero, or Itential payload
# field. The (not yet built) raw normalization layer is responsible for
# turning real command output into these shapes once a real fixture exists.


@dataclass(frozen=True)
class CommandOk:
    parsed: object


@dataclass(frozen=True)
class CommandFailed:
    error: str


@dataclass(frozen=True)
class CommandMissing:
    pass


CommandOutcome = CommandOk | CommandFailed | CommandMissing


@dataclass(frozen=True)
class VersionFacts:
    version: str


@dataclass(frozen=True)
class MlagFacts:
    state: str


@dataclass(frozen=True)
class BgpPeerState:
    peer: str
    established: bool


@dataclass(frozen=True)
class BgpFacts:
    peers: list[BgpPeerState] = field(default_factory=list)


@dataclass(frozen=True)
class InterfaceState:
    name: str
    up: bool


@dataclass(frozen=True)
class InterfacesFacts:
    interfaces: list[InterfaceState] = field(default_factory=list)


@dataclass(frozen=True)
class NormalizedHostData:
    hostname: str
    version: CommandOutcome
    mlag: CommandOutcome
    bgp: CommandOutcome
    interfaces: CommandOutcome


@dataclass(frozen=True)
class NormalizedPairData:
    device_a: NormalizedHostData
    device_b: NormalizedHostData

    def hosts(self) -> list[NormalizedHostData]:
        return [self.device_a, self.device_b]


@dataclass(frozen=True)
class CheckResult:
    status: Status
    reasons: list[str] = field(default_factory=list)
