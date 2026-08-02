"""Canonical deterministic serialization helpers."""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
from enum import Enum
from typing import Any


class CanonicalEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, datetime):
            return obj.astimezone().isoformat()
        if isinstance(obj, Enum):
            return obj.value
        if is_dataclass(obj) and not isinstance(obj, type):
            return asdict(obj)
        return super().default(obj)


def canonical_json(data: Any) -> str:
    return json.dumps(data, cls=CanonicalEncoder, sort_keys=True, separators=(",", ":"))
