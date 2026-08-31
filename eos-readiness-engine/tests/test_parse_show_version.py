import json
from pathlib import Path

import pytest

from eos_readiness.raw.parsers import ParseError, parse_show_version

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "raw"


def load_real_lab01a_output() -> str:
    data = json.loads((FIXTURES_DIR / "USILD001LAB01A__show_version.json").read_text())
    return data["output"]


def test_parses_real_lab01a_fixture():
    facts = parse_show_version(load_real_lab01a_output())
    assert facts.version == "4.31.4M-37710355.4314M"


def test_missing_software_version_line_raises():
    raw = "Arista DCS-7280CR2A-30-F\nHardware version: 21.01\nSerial number: JPE19321543\n"
    with pytest.raises(ParseError):
        parse_show_version(raw)


def test_empty_output_raises():
    with pytest.raises(ParseError):
        parse_show_version("")


def test_malformed_version_line_raises():
    raw = "Software image version:\n"
    with pytest.raises(ParseError):
        parse_show_version(raw)


def test_unrelated_lines_ignored():
    raw = (
        "Arista DCS-7280CR2A-30-F\n"
        "Hardware version: 21.01\n"
        "Software image version: 4.31.4M-37710355.4314M\n"
        "Internal build ID: d26721db-c526-41ec-bf9d-0a14b4edfcf5\n"
        "Total memory: 32738276 kB\n"
    )
    facts = parse_show_version(raw)
    assert facts.version == "4.31.4M-37710355.4314M"


def test_whitespace_variance_tolerated():
    raw = "\n\n   Software image version:   4.31.4M-37710355.4314M   \n\n"
    facts = parse_show_version(raw)
    assert facts.version == "4.31.4M-37710355.4314M"
