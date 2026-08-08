from __future__ import annotations

import argparse
import json
import sys

from eos_ab_upgrade.normalize import normalize_pair_readiness
from eos_ab_upgrade.pair_readiness import evaluate_pair_readiness


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="eos-upgrade", description="EOS A/B upgrade service utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    render = sub.add_parser("render-report", help="Pretty-print a saved evidence report JSON file")
    render.add_argument("report_json", help="Path to a JSON evidence report produced by reporting.to_json()")

    run_precheck = sub.add_parser(
        "precheck",
        help="Normalize + evaluate pair readiness from a JSON payload (canonical contract)",
    )
    run_precheck.add_argument(
        "payload",
        help="Path to a pair payload JSON file (canonical, CVP, or collected side records), or '-' for stdin",
    )

    args = parser.parse_args(argv)

    if args.command == "render-report":
        with open(args.report_json) as f:
            data = json.load(f)
        print(json.dumps(data, indent=2))
        return 0

    if args.command == "precheck":
        if args.payload == "-":
            raw = sys.stdin.read()
        else:
            with open(args.payload) as f:
                raw = f.read()
        payload = json.loads(raw)
        result = evaluate_pair_readiness(normalize_pair_readiness(payload))
        print(json.dumps(result, indent=2))
        return 0 if result["eligible"] else 1

    return 1


if __name__ == "__main__":
    sys.exit(main())
