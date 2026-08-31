from __future__ import annotations

import json
import sys

from .engine import evaluate_pair

# IAG's exact input-passing mechanism for a filename-based python-script is
# unverified (stdin vs. per-field CLI args via the decorator's
# argument_order — see iag/eos-readiness-service.yaml). This assumes stdin;
# confirm against the lab install. Same open question already flagged for
# the sibling eos-ab-upgrade package's iag_entrypoint.py.


def main() -> int:
    payload = json.loads(sys.stdin.read())
    result = evaluate_pair(payload)
    print(json.dumps(result, indent=2))
    return 0 if result["ready"] else 1


if __name__ == "__main__":
    sys.exit(main())
