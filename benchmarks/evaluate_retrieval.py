"""
Đo Recall@K, NDCG@K trên tập benchmark cho hệ thống Retrieval.
"""

import math
from typing import List, Dict, Set


def recall_at_k(relevant_docs: Set[str], retrieved_docs: List[str], k: int) -> float:
    """Calculate Recall@K."""
    if not relevant_docs:
        return 0.0
    top_k_retrieved = set(retrieved_docs[:k])
    hits = len(relevant_docs.intersection(top_k_retrieved))
    return hits / len(relevant_docs)


def dcg_at_k(relevance_scores: List[float], k: int) -> float:
    """Calculate Discounted Cumulative Gain at Rank K."""
    dcg = 0.0
    for i in range(min(len(relevance_scores), k)):
        dcg += (2 ** relevance_scores[i] - 1) / math.log2(i + 2)
    return dcg


def ndcg_at_k(relevant_docs: Dict[str, float], retrieved_docs: List[str], k: int) -> float:
    """Calculate Normalized Discounted Cumulative Gain at Rank K."""
    if not relevant_docs:
        return 0.0

    retrieved_scores = [relevant_docs.get(doc_id, 0.0) for doc_id in retrieved_docs[:k]]
    actual_dcg = dcg_at_k(retrieved_scores, k)

    ideal_scores = sorted(relevant_docs.values(), reverse=True)
    ideal_dcg = dcg_at_k(ideal_scores, k)

    if ideal_dcg == 0.0:
        return 0.0
    return actual_dcg / ideal_dcg


def evaluate_benchmark(benchmark_dataset: List[Dict], k_values: List[int] = [1, 3, 5, 10]):
    """Evaluate retrieval pipeline against benchmark dataset."""
    results = {k: {"recall": 0.0, "ndcg": 0.0} for k in k_values}
    num_queries = len(benchmark_dataset)

    if num_queries == 0:
        print("Empty benchmark dataset.")
        return results

    for item in benchmark_dataset:
        relevant_docs = item["relevant_docs"]  # Dict[str, score] or Set[str]
        retrieved_docs = item["retrieved_docs"]  # List[str]

        rel_set = set(relevant_docs.keys()) if isinstance(relevant_docs, dict) else set(relevant_docs)
        rel_dict = relevant_docs if isinstance(relevant_docs, dict) else {doc: 1.0 for doc in relevant_docs}

        for k in k_values:
            results[k]["recall"] += recall_at_k(rel_set, retrieved_docs, k)
            results[k]["ndcg"] += ndcg_at_k(rel_dict, retrieved_docs, k)

    for k in k_values:
        results[k]["recall"] /= num_queries
        results[k]["ndcg"] /= num_queries
        print(f"Metrics @ K={k}: Recall@{k} = {results[k]['recall']:.4f}, NDCG@{k} = {results[k]['ndcg']:.4f}")

    return results


if __name__ == "__main__":
    # Sample mock evaluation
    sample_data = [
        {
            "query": "What is semantic cache?",
            "relevant_docs": {"doc1": 1.0, "doc3": 0.5},
            "retrieved_docs": ["doc1", "doc2", "doc3", "doc4", "doc5"],
        }
    ]
    evaluate_benchmark(sample_data)
