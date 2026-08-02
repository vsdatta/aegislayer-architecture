"""Evidence record and bundle lifecycle utilities."""

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime

from .exceptions import ValidationError
from .models import ActionRequest, EvidenceBundle, EvidenceRecord, utc_now


@dataclass
class EvidenceBuilder:
    request: ActionRequest
    _records: list[EvidenceRecord]
    _finalized: bool = False

    @classmethod
    def start(cls, request: ActionRequest) -> "EvidenceBuilder":
        return cls(request=request, _records=[])

    def append(self, event_type: str, payload: Mapping[str, str], when: datetime | None = None) -> None:
        if self._finalized:
            raise ValidationError("cannot_append_to_finalized_evidence")
        self._records.append(
            EvidenceRecord(
                event_type=event_type,
                request_id=self.request.request_id,
                correlation_id=self.request.correlation_id,
                causation_id=self.request.causation_id,
                timestamp_utc=when or utc_now(),
                payload=dict(payload),
            )
        )

    def finalize(self, when: datetime | None = None) -> EvidenceBundle:
        self._finalized = True
        return EvidenceBundle(
            request_id=self.request.request_id,
            records=tuple(self._records),
            finalized=True,
            finalized_at=when or utc_now(),
        )
