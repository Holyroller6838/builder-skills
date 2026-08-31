from eos_readiness.raw.collectors import canonicalize_command, group_by_device_and_command


def test_canonicalize_command_maps_sh_mlag_to_show_mlag():
    assert canonicalize_command("sh mlag") == "show mlag"


def test_canonicalize_command_passes_through_unaliased_commands():
    assert canonicalize_command("show version") == "show version"
    assert canonicalize_command("show ip bgp summary") == "show ip bgp summary"
    assert canonicalize_command("show interfaces status") == "show interfaces status"


def test_canonicalize_command_strips_whitespace():
    assert canonicalize_command("  sh mlag  ") == "show mlag"


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


def test_groups_results_by_device_name():
    results = [
        make_result("USILD001LAB01A", "show version"),
        make_result("USILD001LAB01B", "show version"),
    ]
    grouped = group_by_device_and_command(results)
    assert set(grouped.keys()) == {"USILD001LAB01A", "USILD001LAB01B"}


def test_sh_mlag_and_show_mlag_land_in_the_same_canonical_slot():
    results = [make_result("USILD001LAB01A", "sh mlag", output="mlag output")]
    grouped = group_by_device_and_command(results)
    assert "show mlag" in grouped["USILD001LAB01A"]
    entry = grouped["USILD001LAB01A"]["show mlag"]
    assert entry.output == "mlag output"


def test_preserves_output_and_success():
    results = [make_result("USILD001LAB01A", "show version", output="version text", success=False)]
    grouped = group_by_device_and_command(results)
    entry = grouped["USILD001LAB01A"]["show version"]
    assert entry.output == "version text"
    assert entry.success is False


def test_multiple_commands_per_device_all_present():
    results = [
        make_result("USILD001LAB01A", "show version"),
        make_result("USILD001LAB01A", "sh mlag"),
        make_result("USILD001LAB01A", "show ip bgp summary"),
        make_result("USILD001LAB01A", "show interfaces status"),
    ]
    grouped = group_by_device_and_command(results)
    assert set(grouped["USILD001LAB01A"].keys()) == {
        "show version",
        "show mlag",
        "show ip bgp summary",
        "show interfaces status",
    }
