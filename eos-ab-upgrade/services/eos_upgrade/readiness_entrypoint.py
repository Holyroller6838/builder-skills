from __future__ import annotations

import json
import sys

from . import readiness

# IAG's exact input-passing mechanism for a filename-based python-script is unverified
# (stdin vs. per-field CLI args via the decorator's argument_order — see
# iag/eos-readiness-service.yaml). This assumes stdin; confirm against the lab install.


def main() -> int:
    payload = json.loads(sys.stdin.read())
    evidence = readiness.run_readiness_check_from_payload(payload)
    print(json.dumps(evidence, indent=2))
    return 0 if evidence["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
