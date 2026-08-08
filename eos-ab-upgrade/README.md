# eos-ab-upgrade

This package contains decision logic used by an Itential Arista EOS A/B upgrade workflow.

## Layout

```
eos-ab-upgrade/
├── README.md
├── pyproject.toml
├── src/
│   └── eos_ab_upgrade/
│       ├── __init__.py
│       ├── pair_readiness.py
│       ├── gshut_eligibility.py
│       ├── drain_convergence.py
│       ├── post_validation.py
│       └── evidence.py
├── tests/
├── schemas/
└── docs/
```

## Requirements

- Python 3.11+

## Development

```bash
cd eos-ab-upgrade
pip install -e ".[dev]"
pytest -v
```

Business logic is not implemented yet; modules are placeholders pending explicit implementation.
