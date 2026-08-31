from eos_readiness.models import CommandFailed, CommandMissing, CommandOk
from eos_readiness.raw.collectors import group_by_device_and_command
from eos_readiness.raw.normalize import normalize_pair_data

FULL_CHECKS = frozenset({"collection", "version", "interfaces", "mlag", "bgp"})
NO_MLAG_BGP = frozenset({"collection", "version", "interfaces"})


def make_result(name: str, command: str, output: str = "output text", success: bool = True) -> dict:
    return {
        "command": command,
        "elapsed_time": "1.000s",
        "end_time": "2026-08-24T14:52:29Z",
        "host": "10.122.10.130",
        "name": name,
        "output": output,
        "start_time": "2026-08-24T14:52:28Z",
        "success": success,
    }


REAL_VERSION_OUTPUT = "Software image version: 4.31.4M-37710355.4314M\n"


def test_version_parses_successfully_with_real_format():
    results = [make_result("A", "show version", output=REAL_VERSION_OUTPUT)]
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", FULL_CHECKS)
    assert isinstance(pair.device_a.version, CommandOk)
    assert pair.device_a.version.parsed.version == "4.31.4M-37710355.4314M"


def test_command_success_false_becomes_command_failed():
    results = [make_result("A", "show version", output=REAL_VERSION_OUTPUT, success=False)]
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", FULL_CHECKS)
    assert isinstance(pair.device_a.version, CommandFailed)
    assert "success=false" in pair.device_a.version.error


def test_missing_command_becomes_command_missing():
    results = []  # device A has no results at all
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", FULL_CHECKS)
    assert isinstance(pair.device_a.version, CommandMissing)


def test_mlag_not_yet_implemented_becomes_command_failed_with_clear_reason():
    results = [make_result("A", "sh mlag", output="anything")]
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", FULL_CHECKS)
    assert isinstance(pair.device_a.mlag, CommandFailed)
    assert "not yet implemented" in pair.device_a.mlag.error


def test_bgp_not_yet_implemented_becomes_command_failed_with_clear_reason():
    results = [make_result("A", "show ip bgp summary", output="anything")]
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", FULL_CHECKS)
    assert isinstance(pair.device_a.bgp, CommandFailed)
    assert "not yet implemented" in pair.device_a.bgp.error


def test_interfaces_not_yet_implemented_becomes_command_failed_with_clear_reason():
    results = [make_result("A", "show interfaces status", output="anything")]
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", FULL_CHECKS)
    assert isinstance(pair.device_a.interfaces, CommandFailed)
    assert "not yet implemented" in pair.device_a.interfaces.error


def test_mlag_skipped_entirely_when_profile_does_not_require_it():
    # sh mlag IS present in the data, but since the profile doesn't need it,
    # the not-implemented mlag parser must never even be invoked.
    results = [make_result("A", "sh mlag", output="anything")]
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", NO_MLAG_BGP)
    assert isinstance(pair.device_a.mlag, CommandMissing)


def test_bgp_skipped_entirely_when_profile_does_not_require_it():
    results = [make_result("A", "show ip bgp summary", output="anything")]
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", NO_MLAG_BGP)
    assert isinstance(pair.device_a.bgp, CommandMissing)


def test_sh_mlag_alias_is_actually_found_not_treated_as_missing():
    # Distinguishes "found but not-yet-parseable" (CommandFailed) from
    # "alias didn't match, treated as absent" (CommandMissing) — proves the
    # sh mlag -> show mlag canonicalization actually took effect.
    results = [make_result("A", "sh mlag", output="anything")]
    grouped = group_by_device_and_command(results)
    pair = normalize_pair_data(grouped, "A", "B", FULL_CHECKS)
    assert isinstance(pair.device_a.mlag, CommandFailed)
    assert "not yet implemented" in pair.device_a.mlag.error
