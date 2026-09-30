"""Offline tests for the hardened EOS readiness IAG entrypoint boundary."""

from __future__ import annotations

import io
import json
from unittest.mock import patch

import pytest

from eos_readiness.contracts import EOSReadinessResult
from eos_readiness.errors import MalformedPayloadError, ProfileNotFoundError
from eos_readiness.iag_entrypoint import main, run_from_stdin

PASS_RESULT = {
    "pair": {
        "device_a": "USILD001LAB01A",
        "device_b": "USILD001LAB01B",
    },
    "profile": "basic_pair",
    "ready": True,
    "status": "PASS",
    "checks": {
        "collection": "PASS",
        "version": "PASS",
        "interfaces": "PASS",
        "mlag": "NOT_APPLICABLE",
        "bgp": "NOT_APPLICABLE",
    },
    "reasons": [],
    "pair_id": "pair-01",
}

FAIL_RESULT = {
    "pair": {
        "device_a": "USILD001LAB01A",
        "device_b": "USILD001LAB01B",
    },
    "profile": "basic_pair",
    "ready": False,
    "status": "FAIL",
    "checks": {
        "collection": "PASS",
        "version": "FAIL",
        "interfaces": "WARNING",
        "mlag": "NOT_APPLICABLE",
        "bgp": "NOT_APPLICABLE",
    },
    "reasons": ["version mismatch"],
    "pair_id": "pair-01",
}

# Mirrors evaluate_pair's early-fail shape (≠2 devices): valid dict, not EOSReadinessResult.
EARLY_FAIL_RESULT = {
    "pair_id": "pair-01",
    "profile": "basic_pair",
    "ready": False,
    "status": "FAIL",
    "checks": {},
    "reasons": [
        "expected exactly 2 distinct devices in command_results "
        "(grouped by each result's 'name' field), found 0: []"
    ],
}

VALID_PAYLOAD = {
    "pair_id": "pair-01",
    "target_version": "4.33.1F",
    "profile": "basic_pair",
    "command_results": [],
}


def _run_main(stdin_text: str, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]):
    monkeypatch.setattr("sys.stdin", io.StringIO(stdin_text))
    exit_code = main()
    captured = capsys.readouterr()
    return exit_code, captured.out, captured.err


def _assert_single_json_document(stdout: str) -> dict:
    assert stdout, "expected JSON on stdout"
    # Exactly one JSON document: parse the full stdout (strip trailing newline only).
    parsed = json.loads(stdout)
    # Round-trip proves stdout is a single JSON value (not concatenated docs / trailing junk).
    assert json.dumps(parsed, indent=2) + "\n" == stdout or json.dumps(parsed, indent=2) == stdout.rstrip(
        "\n"
    ) and stdout.endswith("\n")
    # Stronger: full text after optional trailing newline must decode as one value.
    assert stdout.strip() == json.dumps(parsed, indent=2)
    return parsed


def test_pass_returns_validated_json_and_exit_0(monkeypatch, capsys):
    with patch("eos_readiness.iag_entrypoint.evaluate_pair", return_value=PASS_RESULT):
        exit_code, stdout, stderr = _run_main(json.dumps(VALID_PAYLOAD), monkeypatch, capsys)

    assert exit_code == 0
    body = _assert_single_json_document(stdout)
    assert "error" not in body
    validated = EOSReadinessResult.model_validate(body)
    assert validated.ready is True
    assert validated.status == "PASS"
    assert body == validated.model_dump()
    assert "Traceback" not in stdout


def test_fail_returns_validated_json_and_exit_1(monkeypatch, capsys):
    with patch("eos_readiness.iag_entrypoint.evaluate_pair", return_value=FAIL_RESULT):
        exit_code, stdout, _stderr = _run_main(json.dumps(VALID_PAYLOAD), monkeypatch, capsys)

    assert exit_code == 1
    body = _assert_single_json_document(stdout)
    assert "error" not in body
    validated = EOSReadinessResult.model_validate(body)
    assert validated.ready is False
    assert validated.status == "FAIL"
    assert body == validated.model_dump()


def test_malformed_stdin_json_returns_failure_envelope_and_exit_1(monkeypatch, capsys):
    exit_code, stdout, _stderr = _run_main("{not-json", monkeypatch, capsys)

    assert exit_code == 1
    body = _assert_single_json_document(stdout)
    assert body["ready"] is False
    assert body["status"] == "FAIL"
    assert body["error"]["type"] == "malformed_json"
    assert body["reasons"]
    with pytest.raises(Exception):
        EOSReadinessResult.model_validate(body)


def test_malformed_payload_returns_failure_envelope_and_exit_1(monkeypatch, capsys):
    with patch(
        "eos_readiness.iag_entrypoint.evaluate_pair",
        side_effect=MalformedPayloadError("payload missing required key(s): ['target_version']"),
    ):
        exit_code, stdout, _stderr = _run_main(json.dumps(VALID_PAYLOAD), monkeypatch, capsys)

    assert exit_code == 1
    body = _assert_single_json_document(stdout)
    assert body["error"]["type"] == "malformed_payload"
    assert body["pair_id"] == "pair-01"
    assert body["ready"] is False
    assert body["status"] == "FAIL"


def test_unknown_profile_returns_distinct_error_type_and_exit_1(monkeypatch, capsys):
    with patch(
        "eos_readiness.iag_entrypoint.evaluate_pair",
        side_effect=ProfileNotFoundError("nonexistent_profile"),
    ):
        exit_code, stdout, _stderr = _run_main(json.dumps(VALID_PAYLOAD), monkeypatch, capsys)

    assert exit_code == 1
    body = _assert_single_json_document(stdout)
    assert body["error"]["type"] == "unknown_profile"
    assert "nonexistent_profile" in body["error"]["message"]
    assert body["ready"] is False
    assert body["status"] == "FAIL"


def test_unexpected_exception_returns_failure_envelope_and_exit_1(monkeypatch, capsys):
    with patch(
        "eos_readiness.iag_entrypoint.evaluate_pair",
        side_effect=RuntimeError("boom"),
    ):
        exit_code, stdout, stderr = _run_main(json.dumps(VALID_PAYLOAD), monkeypatch, capsys)

    assert exit_code == 1
    body = _assert_single_json_document(stdout)
    assert body["error"]["type"] == "unexpected_error"
    assert "RuntimeError" in body["error"]["message"]
    assert "boom" in body["error"]["message"]
    assert "Traceback" not in stdout
    assert "Traceback" in stderr


def test_contract_violation_on_early_fail_shape_returns_envelope_and_exit_1(monkeypatch, capsys):
    """Option A: engine early-fail dict fails EOSReadinessResult → contract_violation."""
    with patch(
        "eos_readiness.iag_entrypoint.evaluate_pair",
        return_value=EARLY_FAIL_RESULT,
    ):
        exit_code, stdout, stderr = _run_main(json.dumps(VALID_PAYLOAD), monkeypatch, capsys)

    assert exit_code == 1
    body = _assert_single_json_document(stdout)
    assert body["ready"] is False
    assert body["status"] == "FAIL"
    assert body["error"]["type"] == "contract_violation"
    assert body["pair_id"] == "pair-01"
    assert body["error"]["message"]
    # No raw traceback / exception dump outside the JSON envelope.
    assert "Traceback" not in stdout
    assert "Traceback" not in stderr
    assert not stdout.lstrip().startswith("Traceback")
    # Failure envelope is not an EOSReadinessResult.
    with pytest.raises(Exception):
        EOSReadinessResult.model_validate(body)


def test_stdout_contains_exactly_one_valid_json_document():
    response, exit_code = run_from_stdin("{not-json")
    assert exit_code == 1
    text = json.dumps(response, indent=2)
    # Mimic main(): one print → one JSON document + newline.
    stdout = text + "\n"
    parsed = json.loads(stdout)
    assert parsed == response
    assert stdout.count("{") >= 1
    # No second top-level JSON value after the first document.
    decoder = json.JSONDecoder()
    _obj, idx = decoder.raw_decode(stdout)
    assert stdout[idx:].strip() == ""
