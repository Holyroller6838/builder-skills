"""BGP_Traffic_Drain service input contract.

Strict request shape for enter/exit traffic-drain operations against an
Arista EOS A/B pair. IAG transport metadata is excluded.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict

DrainOperation = Literal["enter", "exit"]


class BGPTrafficDrainRequest(BaseModel):
    """Strict business input for the BGP_Traffic_Drain IAG service boundary."""

    model_config = ConfigDict(extra="forbid")

    device_a: str
    device_b: str
    operation: DrainOperation
