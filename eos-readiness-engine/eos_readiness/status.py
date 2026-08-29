from __future__ import annotations

from collections.abc import Iterable
from enum import Enum


class Status(str, Enum):
    PASS = "PASS"
    WARNING = "WARNING"
    FAIL = "FAIL"
    NOT_APPLICABLE = "NOT_APPLICABLE"


_SEVERITY = {Status.FAIL: 3, Status.WARNING: 2, Status.PASS: 1}


def worst_of(statuses: Iterable[Status]) -> Status:
    applicable = [s for s in statuses if s != Status.NOT_APPLICABLE]
    if not applicable:
        return Status.PASS
    return max(applicable, key=lambda s: _SEVERITY[s])
