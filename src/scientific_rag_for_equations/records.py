"""Structured records for grounded scientific retrieval."""
from __future__ import annotations
import re
from dataclasses import dataclass
@dataclass(frozen=True)
class Evidence:
    source_id: str
    quote: str
    locator: str

def normalize_equation(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("−", "-")).strip()

def require_evidence(answer: str, evidence: list[Evidence]) -> dict:
    return {"answer": answer, "evidence": [e.__dict__ for e in evidence], "grounded": bool(evidence)}
