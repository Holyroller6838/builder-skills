from __future__ import annotations

import argparse
import json
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="eos-upgrade", description="EOS A/B upgrade service utilities")
    sub = parser.add_subparsers(dest="command", required=True)

    render = sub.add_parser("render-report", help="Pretty-print a saved evidence report JSON file")
    render.add_argument("report_json", help="Path to a JSON evidence report produced by reporting.to_json()")

    args = parser.parse_args(argv)

    if args.command == "render-report":
        with open(args.report_json) as f:
            data = json.load(f)
        print(json.dumps(data, indent=2))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
