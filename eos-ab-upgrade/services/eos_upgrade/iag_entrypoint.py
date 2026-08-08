from __future__ import annotations

import json
import sys

from eos_ab_upgrade.normalize import normalize_pair_readiness
from eos_ab_upgrade.pair_readiness import evaluate_pair_readiness

# IAG's exact input-passing mechanism for a filename-based python-script is unverified
# (stdin vs. per-field CLI args via the decorator's argument_order — see
# iag/eos-precheck-service.yaml). This assumes stdin; confirm against the lab install.
#
# Input contract: raw Itential/CVP/Device Broker payloads are accepted and
# normalized into schemas/pair_readiness.canonical.json before evaluation.
# evaluate_pair_readiness() never sees vendor-specific shapes.


def main() -> int:
    payload = json.loads(sys.stdin.read())
    canonical = normalize_pair_readiness(payload)
    result = evaluate_pair_readiness(canonical)
    print(json.dumps(result, indent=2))
    return 0 if result["eligible"] else 1


if __name__ == "__main__":
    sys.exit(main())
