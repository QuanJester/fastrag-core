"""Hybrid Search combining Qdrant client (Dense retrieval) and Tantivy (Sparse/BM25 retrieval)."""

from typing import List, Dict, Any


class HybridRetriever:
    """Combines vector search from Qdrant with BM25 full-text search from Tantivy."""

    def __init__(self, qdrant_client=None, tantivy_index=None):
        self.qdrant_client = qdrant_client
        self.tantivy_index = tantivy_index

    async def search_dense(self, query_vector: List[float], top_k: int = 20) -> List[Dict[str, Any]]:
        """Dense semantic search using Qdrant."""
        # e.g., self.qdrant_client.search(...)
        return []

    async def search_sparse(self, query_text: str, top_k: int = 20) -> List[Dict[str, Any]]:
        """Sparse BM25 keyword search using Tantivy."""
        # e.g., self.tantivy_index.searcher().search(...)
        return []

    async def hybrid_search(self, query_text: str, query_vector: List[float], top_k: int = 20) -> Dict[str, List[Dict[str, Any]]]:
        """Fetch both dense and sparse retrieval results for downstream fusion."""
        dense_results = await self.search_dense(query_vector, top_k=top_k)
        sparse_results = await self.search_sparse(query_text, top_k=top_k)
        return {
            "dense": dense_results,
            "sparse": sparse_results,
        }
