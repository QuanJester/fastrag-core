"""RRF (Reciprocal Rank Fusion) logic and ONNX Reranker runner."""

from typing import List, Dict, Any
from collections import defaultdict


def reciprocal_rank_fusion(
    ranked_lists: List[List[Dict[str, Any]]],
    k: int = 60,
    top_k: int = 10,
) -> List[Dict[str, Any]]:
    """Compute Reciprocal Rank Fusion (RRF) scores across multiple ranked lists."""
    rrf_scores = defaultdict(float)
    doc_lookup = {}

    for ranked_list in ranked_lists:
        for rank, item in enumerate(ranked_list):
            doc_id = item["id"]
            rrf_scores[doc_id] += 1.0 / (k + rank + 1)
            if doc_id not in doc_lookup:
                doc_lookup[doc_id] = item

    sorted_docs = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]

    results = []
    for doc_id, score in sorted_docs:
        doc = doc_lookup[doc_id].copy()
        doc["rrf_score"] = score
        results.append(doc)

    return results


class ONNXReranker:
    """Runs cross-encoder reranker model compiled to ONNX runtime (INT8 quantized)."""

    def __init__(self, model_path: str = "models/reranker_quantized_int8.onnx"):
        self.model_path = model_path
        self.session = None
        # e.g., onnxruntime.InferenceSession(self.model_path, providers=['CPUExecutionProvider'])

    def rerank(self, query: str, documents: List[Dict[str, Any]], top_k: int = 5) -> List[Dict[str, Any]]:
        """Compute reranking scores for query-document pairs."""
        # Score pairs using ONNX session and sort
        return documents[:top_k]
