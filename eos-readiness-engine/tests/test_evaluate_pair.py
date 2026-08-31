import json
from pathlib import Path

import pytest

from eos_readiness.engine import evaluate_pair
from eos_readiness.errors import MalformedPayloadError, ProfileNotFoundError

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "raw"


def load_pair_command_results() -> list[dict]:
    data = json.loads((FIXTURES_DIR / "command_results_pair_sample.json").read_text())
    return data["results"]


def make_payload(**overrides) -> dict:
    payload = {
        "pair_id": "pair-01",
        "target_version": "4.31.4M-37710355.4314M",
        "profile": "mlag_bgp",
        "command_results": load_pair_command_results(),
    }
    payload.update(overrides)
    return payload


def test_current_state_fails_closed_pending_unimplemented_parsers():
    # Honest, expected current behavior: version parses fine and matches,
    # but mlag/bgp/interfaces have no real parser yet, so the overall result
    # is FAIL with clear "not yet implemented" reasons — not a silent PASS.
    result = evaluate_pair(make_payload())
    assert result["status"] == "FAIL"
    assert result["ready"] is False
    assert result["pair_id"] == "pair-01"
    assert any("not yet implemented" in r for r in result["reasons"])


def test_basic_pair_profile_marks_mlag_and_bgp_not_applicable():
    result = evaluate_pair(make_payload(profile="basic_pair"))
    assert result["checks"]["mlag"] == "NOT_APPLICABLE"
    assert result["checks"]["bgp"] == "NOT_APPLICABLE"
    # interfaces still isn't implemented, so this profile still fails closed —
    # but never because of mlag/bgp, which correctly never even ran.
    assert result["status"] == "FAIL"
    assert not any("mlag" in r.lower() for r in result["reasons"])
    assert not any("bgp" in r.lower() for r in result["reasons"])


def test_bgp_only_profile_marks_mlag_not_applicable():
    result = evaluate_pair(make_payload(profile="bgp_only"))
    assert result["checks"]["mlag"] == "NOT_APPLICABLE"
    assert result["checks"]["bgp"] != "NOT_APPLICABLE"


def test_version_check_passes_on_its_own_when_target_matches():
    # Isolates that version parsing + comparison genuinely works end-to-end
    # through the full entrypoint, independent of the other unimplemented checks.
    result = evaluate_pair(make_payload())
    assert result["checks"]["version"] == "PASS"


def test_missing_top_level_key_raises_malformed_payload_error():
    payload = make_payload()
    del payload["target_version"]
    with pytest.raises(MalformedPayloadError, match="target_version"):
        evaluate_pair(payload)


def test_unknown_profile_raises_profile_not_found_error():
    with pytest.raises(ProfileNotFoundError):
        evaluate_pair(make_payload(profile="nonexistent_profile"))


def test_zero_devices_in_command_results_fails_closed_without_raising():
    result = evaluate_pair(make_payload(command_results=[]))
    assert result["status"] == "FAIL"
    assert result["ready"] is False
    assert result["checks"] == {}
    assert any("found 0" in r for r in result["reasons"])


def test_single_device_in_command_results_fails_closed_without_raising():
    all_results = load_pair_command_results()
    only_a = [r for r in all_results if r["name"] == "USILD001LAB01A"]
    result = evaluate_pair(make_payload(command_results=only_a))
    assert result["status"] == "FAIL"
    assert result["ready"] is False
    assert result["checks"] == {}
    assert any("found 1" in r for r in result["reasons"])


def test_three_devices_in_command_results_fails_closed_without_raising():
    all_results = load_pair_command_results()
    extra = dict(all_results[0])
    extra["name"] = "USILD001LAB01C"
    result = evaluate_pair(make_payload(command_results=all_results + [extra]))
    assert result["status"] == "FAIL"
    assert result["checks"] == {}
    assert any("found 3" in r for r in result["reasons"])


def test_output_is_json_serializable():
    result = evaluate_pair(make_payload())
    json.dumps(result)  # must not raise
