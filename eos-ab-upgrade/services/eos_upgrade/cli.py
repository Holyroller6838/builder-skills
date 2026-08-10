from __future__ import annotations

import argparse
import json
import sys

from . import precheck, readiness


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="eos-upgrade", description="EOS A/B upgrade service utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    render = sub.add_parser("render-report", help="Pretty-print a saved evidence report JSON file")
    render.add_argument("report_json", help="Path to a JSON evidence report produced by reporting.to_json()")

    run_precheck = sub.add_parser("precheck", help="Run the read-only EOS A/B precheck from a JSON payload")
    run_precheck.add_argument("payload", help="Path to a precheck payload JSON file, or '-' to read from stdin")

    run_readiness = sub.add_parser(
        "readiness", help="Run the read-only single-device EOS upgrade readiness check from a JSON payload"
    )
    run_readiness.add_argument("payload", help="Path to a readiness payload JSON file, or '-' to read from stdin")

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
        evidence = precheck.run_pre_check_from_payload(payload)
        print(json.dumps(evidence, indent=2))
        return 0 if evidence["passed"] else 1

    if args.command == "readiness":
        if args.payload == "-":
            raw = sys.stdin.read()
        else:
            with open(args.payload) as f:
                raw = f.read()
        payload = json.loads(raw)
        evidence = readiness.run_readiness_check_from_payload(payload)
        print(json.dumps(evidence, indent=2))
        return 0 if evidence["passed"] else 1

    return 1


if __name__ == "__main__":
    sys.exit(main())
