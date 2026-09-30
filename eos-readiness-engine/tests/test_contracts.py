"""Contract-layer tests for EOS_Readiness and BGP_Traffic_Drain models.

These validate the Pydantic v2 boundaries only — production services are
not yet integrated with these models.
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from eos_readiness.contracts import BGPTrafficDrainRequest, EOSReadinessResult

VALID_READINESS = {
    "pair": {
        "device_a": "USILD001LAB01A",
        "device_b": "USILD001LAB01B",
    },
    "profile": "basic_pair",
    "ready": False,
    "status": "FAIL",
    "checks": {
        "collection": "PASS",
        "version": "FAIL",
        "interfaces": "WARNING",
        "mlag": "NOT_APPLICABLE",
        "bgp": "NOT_APPLICABLE",
    },
    "reasons": [],
    "pair_id": "pair-01",
}

VALID_BGP_DRAIN = {
    "device_a": "USILD001LAB01A",
    "device_b": "USILD001LAB01B",
    "operation": "enter",
}

IAG_TRANSPORT_EXTRAS = {
    "executionGateway": "lab-gw-01",
    "jsonrpc": "2.0",
    "id": "req-123",
    "receiveTime": "2026-09-29T16:00:00Z",
    "return_code": 0,
    "stdout": "{}",
}


def test_valid_readiness_result():
    result = EOSReadinessResult.model_validate(VALID_READINESS)
    assert result.pair.device_a == "USILD001LAB01A"
    assert result.pair.device_b == "USILD001LAB01B"
    assert result.profile == "basic_pair"
    assert result.ready is False
    assert result.status == "FAIL"
    assert result.checks.collection == "PASS"
    assert result.checks.version == "FAIL"
    assert result.checks.interfaces == "WARNING"
    assert result.checks.mlag == "NOT_APPLICABLE"
    assert result.checks.bgp == "NOT_APPLICABLE"
    assert result.reasons == []
    assert result.pair_id == "pair-01"


def test_valid_bgp_drain_request():
    request = BGPTrafficDrainRequest.model_validate(VALID_BGP_DRAIN)
    assert request.device_a == "USILD001LAB01A"
    assert request.device_b == "USILD001LAB01B"
    assert request.operation == "enter"

    exit_request = BGPTrafficDrainRequest.model_validate(
        {**VALID_BGP_DRAIN, "operation": "exit"}
    )
    assert exit_request.operation == "exit"


def test_invalid_operation():
    with pytest.raises(ValidationError) as exc_info:
        BGPTrafficDrainRequest.model_validate(
            {**VALID_BGP_DRAIN, "operation": "drain"}
        )
    assert "operation" in str(exc_info.value)


@pytest.mark.parametrize("missing_field", ["device_a", "device_b"])
def test_missing_device_a_or_device_b(missing_field):
    payload = dict(VALID_BGP_DRAIN)
    del payload[missing_field]
    with pytest.raises(ValidationError) as exc_info:
        BGPTrafficDrainRequest.model_validate(payload)
    assert missing_field in str(exc_info.value)


def test_extra_iag_fields_are_rejected():
    with pytest.raises(ValidationError) as exc_info:
        EOSReadinessResult.model_validate({**VALID_READINESS, **IAG_TRANSPORT_EXTRAS})
    assert "extra" in str(exc_info.value).lower() or any(
        key in str(exc_info.value) for key in IAG_TRANSPORT_EXTRAS
    )

    with pytest.raises(ValidationError) as exc_info:
        BGPTrafficDrainRequest.model_validate({**VALID_BGP_DRAIN, **IAG_TRANSPORT_EXTRAS})
    assert "extra" in str(exc_info.value).lower() or any(
        key in str(exc_info.value) for key in IAG_TRANSPORT_EXTRAS
    )


def test_model_serialization_with_model_dump():
    result = EOSReadinessResult.model_validate(VALID_READINESS)
    dumped = result.model_dump()
    assert dumped == VALID_READINESS

    request = BGPTrafficDrainRequest.model_validate(VALID_BGP_DRAIN)
    assert request.model_dump() == VALID_BGP_DRAIN


def test_json_schema_generation_with_model_json_schema():
    readiness_schema = EOSReadinessResult.model_json_schema()
    assert readiness_schema["type"] == "object"
    assert "pair" in readiness_schema["properties"]
    assert "status" in readiness_schema["properties"]
    assert "checks" in readiness_schema["properties"]
    assert readiness_schema.get("additionalProperties") is False

    drain_schema = BGPTrafficDrainRequest.model_json_schema()
    assert drain_schema["type"] == "object"
    assert set(drain_schema["required"]) == {"device_a", "device_b", "operation"}
    assert drain_schema.get("additionalProperties") is False
    operation = drain_schema["properties"]["operation"]
    assert set(operation.get("enum", [])) == {"enter", "exit"}
