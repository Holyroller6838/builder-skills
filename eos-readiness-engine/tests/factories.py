from __future__ import annotations

from eos_readiness.models import (
    BgpFacts,
    BgpPeerState,
    CommandMissing,
    CommandOk,
    InterfacesFacts,
    InterfaceState,
    MlagFacts,
    NormalizedHostData,
    NormalizedPairData,
    VersionFacts,
)


def ok_version(version: str = "4.33.1F") -> CommandOk:
    return CommandOk(VersionFacts(version=version))


def ok_mlag(state: str = "active") -> CommandOk:
    return CommandOk(MlagFacts(state=state))


def ok_bgp(peers: list[tuple[str, bool]] | None = None) -> CommandOk:
    if peers is None:
        peers = [("10.0.0.1", True), ("10.0.0.2", True)]
    return CommandOk(BgpFacts(peers=[BgpPeerState(peer, established) for peer, established in peers]))


def ok_interfaces(interfaces: list[tuple[str, bool]] | None = None) -> CommandOk:
    if interfaces is None:
        interfaces = [("Ethernet1", True), ("Ethernet2", True)]
    return CommandOk(InterfacesFacts(interfaces=[InterfaceState(name, up) for name, up in interfaces]))


def make_host(
    hostname: str,
    *,
    version=None,
    mlag=None,
    bgp=None,
    interfaces=None,
) -> NormalizedHostData:
    return NormalizedHostData(
        hostname=hostname,
        version=version if version is not None else ok_version(),
        mlag=mlag if mlag is not None else ok_mlag(),
        bgp=bgp if bgp is not None else ok_bgp(),
        interfaces=interfaces if interfaces is not None else ok_interfaces(),
    )


def missing_host(hostname: str) -> NormalizedHostData:
    return NormalizedHostData(
        hostname=hostname,
        version=CommandMissing(),
        mlag=CommandMissing(),
        bgp=CommandMissing(),
        interfaces=CommandMissing(),
    )


def make_pair(host_a: NormalizedHostData | None = None, host_b: NormalizedHostData | None = None) -> NormalizedPairData:
    return NormalizedPairData(
        device_a=host_a or make_host("USILD001LAB01A"),
        device_b=host_b or make_host("USILD001LAB01B"),
    )
