"""EOS_Readiness service output contract.

Mirrors the business decision payload returned by
``eos_readiness.engine.evaluate_pair`` / ``evaluate_normalized`` (plus
``pair_id`` from the pair entrypoint). IAG transport metadata is excluded.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

CheckStatus = Literal["PASS", "WARNING", "FAIL", "NOT_APPLICABLE"]
OverallStatus = Literal["PASS", "WARNING", "FAIL"]


class EOSReadinessPair(BaseModel):
    """Device pair identity in a readiness result."""

    model_config = ConfigDict(extra="forbid")

    device_a: str
    device_b: str


class EOSReadinessChecks(BaseModel):
    """Per-check status roll-up for a readiness evaluation."""

    model_config = ConfigDict(extra="forbid")

    collection: CheckStatus
    version: CheckStatus
    interfaces: CheckStatus
    mlag: CheckStatus
    bgp: CheckStatus


class EOSReadinessResult(BaseModel):
    """Strict business output for the EOS_Readiness IAG service boundary."""

    model_config = ConfigDict(extra="forbid")

    pair: EOSReadinessPair
    profile: str
    ready: bool
    status: OverallStatus
    checks: EOSReadinessChecks
    reasons: list[str] = Field(default_factory=list)
    pair_id: str
