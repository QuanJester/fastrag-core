"""Stress testing scripts for FastRAG API using Locust."""

from locust import HttpUser, task, between
import random


class FastRAGUser(HttpUser):
    wait_time = between(0.1, 1.0)

    sample_queries = [
        "What is FastRAG?",
        "How does semantic caching work?",
        "Explain hybrid search with Tantivy and Qdrant.",
        "What is Reciprocal Rank Fusion (RRF)?",
        "How to quantize ONNX models to INT8?",
        "What are the benefits of vector embeddings?",
    ]

    @task(3)
    def test_search_query(self):
        query = random.choice(self.sample_queries)
        payload = {"query": query, "top_k": 5}
        self.client.post("/api/v1/search", json=payload)

    @task(2)
    def test_ask_stream(self):
        query = random.choice(self.sample_queries)
        payload = {"query": query, "stream": True}
        self.client.post("/api/v1/ask", json=payload)

    @task(1)
    def test_health_check(self):
        self.client.get("/health")
