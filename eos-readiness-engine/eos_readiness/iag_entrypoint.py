from __future__ import annotations

import json
import sys
import traceback
from typing import Literal

from pydantic import ValidationError

from .contracts import EOSReadinessResult
from .engine import evaluate_pair
from .errors import MalformedPayloadError, ProfileNotFoundError

# IAG's exact input-passing mechanism for a filename-based python-script is
# unverified (stdin vs. per-field CLI args via the decorator's
# argument_order — see iag/eos-readiness-service.yaml). This assumes stdin;
# confirm against the lab install. Same open question already flagged for
# the sibling eos-ab-upgrade package's iag_entrypoint.py.

ErrorType = Literal[
    "malformed_json",
    "malformed_payload",
    "unknown_profile",
    "contract_violation",
    "unexpected_error",
]


def build_failure_response(
    *,
    error_type: ErrorType,
    message: str,
    pair_id: str | None = None,
) -> dict:
    """Predictable failure envelope — separate from EOSReadinessResult."""
    response: dict = {
        "ready": False,
        "status": "FAIL",
        "error": {
            "type": error_type,
            "message": message,
        },
        "reasons": [message],
    }
    if pair_id is not None:
        response["pair_id"] = pair_id
    return response


def _pair_id_from_payload(payload: object) -> str | None:
    if isinstance(payload, dict):
        value = payload.get("pair_id")
        if isinstance(value, str):
            return value
    return None


def run_from_payload(payload: dict) -> tuple[dict, int]:
    """Evaluate + contract-validate. Returns (response_dict, exit_code)."""
    pair_id = _pair_id_from_payload(payload)
    try:
        result = evaluate_pair(payload)
    except MalformedPayloadError as exc:
        return (
            build_failure_response(
                error_type="malformed_payload",
                message=str(exc),
                pair_id=pair_id,
            ),
            1,
        )
    except ProfileNotFoundError as exc:
        return (
            build_failure_response(
                error_type="unknown_profile",
                message=str(exc),
                pair_id=pair_id,
            ),
            1,
        )
    except Exception as exc:
        traceback.print_exc(file=sys.stderr)
        return (
            build_failure_response(
                error_type="unexpected_error",
                message=f"{type(exc).__name__}: {exc}",
                pair_id=pair_id,
            ),
            1,
        )

    try:
        validated = EOSReadinessResult.model_validate(result)
    except ValidationError as exc:
        return (
            build_failure_response(
                error_type="contract_violation",
                message=str(exc),
                pair_id=pair_id if pair_id is not None else result.get("pair_id"),
            ),
            1,
        )

    dumped = validated.model_dump()
    return dumped, (0 if dumped["ready"] else 1)


def run_from_stdin(stdin_text: str) -> tuple[dict, int]:
    """Parse JSON, then run_from_payload. Handles JSONDecodeError."""
    try:
        payload = json.loads(stdin_text)
    except json.JSONDecodeError as exc:
        return (
            build_failure_response(
                error_type="malformed_json",
                message=str(exc),
            ),
            1,
        )

    if not isinstance(payload, dict):
        return (
            build_failure_response(
                error_type="malformed_payload",
                message=f"payload must be a JSON object, got {type(payload).__name__}",
            ),
            1,
        )

    return run_from_payload(payload)


def main() -> int:
    """Read stdin, print exactly one JSON object to stdout, return exit code."""
    response, exit_code = run_from_stdin(sys.stdin.read())
    print(json.dumps(response, indent=2))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
