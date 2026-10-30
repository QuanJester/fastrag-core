"""Pydantic schemas for FastRAG API requests and responses."""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class SearchRequest(BaseModel):
    query: str = Field(..., description="Query string to search")
    top_k: int = Field(5, description="Number of documents to return", ge=1, le=50)
    use_cache: bool = Field(True, description="Whether to check semantic and exact cache")


class DocumentResult(BaseModel):
    id: str
    content: str
    score: float
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SearchResponse(BaseModel):
    query: str
    results: List[DocumentResult]
    cached: bool = False
    cache_type: Optional[str] = None
    latency_ms: float = 0.0


class AskRequest(BaseModel):
    query: str = Field(..., description="User question")
    stream: bool = Field(False, description="Whether to use SSE streaming response")
    top_k: int = Field(5, description="Context retrieval size")


class AskResponse(BaseModel):
    query: str
    answer: str
    sources: List[DocumentResult]
    latency_ms: float = 0.0
