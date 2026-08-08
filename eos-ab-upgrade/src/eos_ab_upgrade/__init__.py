"""Decision logic for Itential Arista EOS A/B upgrade workflows."""

from .normalize import normalize_pair_readiness
from .pair_readiness import evaluate_pair_readiness

__all__ = ["evaluate_pair_readiness", "normalize_pair_readiness"]
