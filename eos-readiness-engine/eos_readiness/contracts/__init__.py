"""Strict Pydantic v2 I/O contracts for EOS upgrade IAG service boundaries.

These models are intentionally not wired into production entrypoints yet.
They define reusable shapes for EOS_Readiness outputs and BGP_Traffic_Drain
inputs without changing existing service behavior.
"""

from .bgp_drain import BGPTrafficDrainRequest
from .readiness import (
    CheckStatus,
    EOSReadinessChecks,
    EOSReadinessPair,
    EOSReadinessResult,
    OverallStatus,
)

__all__ = [
    "BGPTrafficDrainRequest",
    "CheckStatus",
    "EOSReadinessChecks",
    "EOSReadinessPair",
    "EOSReadinessResult",
    "OverallStatus",
]
