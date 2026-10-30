"""Environment configs and threshold parameters for FastRAG."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App configs
    APP_NAME: str = "fastrag-core"
    APP_ENV: str = "development"
    DEBUG: bool = True
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    # Redis (Cache)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    REDIS_PASSWORD: Optional[str] = None
    CACHE_TTL_SECONDS: int = 3600
    EXACT_CACHE_ENABLED: bool = True
    SEMANTIC_CACHE_ENABLED: bool = True
    SEMANTIC_CACHE_THRESHOLD: float = 0.92

    # Qdrant (Vector DB)
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "fastrag_documents"

    # Tantivy (BM25 Fulltext index)
    TANTIVY_INDEX_PATH: str = "./tantivy_index"

    # Retrieval & Ranking Parameters
    TOP_K_DENSE: int = 20
    TOP_K_SPARSE: int = 20
    RRF_K: int = 60
    FINAL_TOP_K: int = 5

    # Models & Weights
    EMBEDDING_MODEL_PATH: str = "models/embedding_model.onnx"
    RERANKER_MODEL_PATH: str = "models/reranker_quantized_int8.onnx"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
