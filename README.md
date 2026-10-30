# FastRAG Core

High-performance Retrieval-Augmented Generation (RAG) system with hybrid search, multi-level caching, and ONNX runtime reranking.

## 📁 Project Structure

```text
fastrag-core/
├── docker/
│   ├── docker-compose.yml    # Qdrant, Redis, Prometheus, Grafana
│   └── Dockerfile
├── benchmarks/
│   ├── locustfile.py         # Stress testing scripts
│   └── evaluate_retrieval.py # Đo Recall@K, NDCG@K trên tập benchmark
├── src/
│   ├── api/                  # FastAPI route, SSE streaming, schemas
│   ├── core/
│   │   ├── cache/            # Exact & Semantic Cache (Redis)
│   │   ├── retrieval/        # Hybrid Search (Qdrant client + Tantivy)
│   │   ├── ranking/          # RRF logic & ONNX Reranker runner
│   │   └── ingestion/        # Chunking, parsing, document indexing
│   ├── config.py             # Environment configs, threshold parameters
│   └── main.py               # Application entrypoint
├── models/                   # Chứa file weights .onnx (INT8 quantized)
└── README.md
```

---

## 🚀 Key Features

- **Hybrid Search**: Dense retrieval via **Qdrant** and BM25 full-text sparse retrieval via **Tantivy**.
- **Multi-level Caching**: Exact hash caching and vector semantic caching backed by **Redis**.
- **RRF & ONNX Reranker**: Reciprocal Rank Fusion (RRF) and optimized INT8 quantized cross-encoder models via **ONNX Runtime**.
- **High-throughput API**: Built with **FastAPI**, supporting Server-Sent Events (SSE) streaming.
- **Monitoring & Benchmarks**: Pre-configured **Prometheus** & **Grafana** alongside **Locust** stress testing scripts and Recall@K / NDCG@K evaluation metrics.

---

## 🛠️ Getting Started

### 1. Start Infrastructure Services

```bash
cd docker
docker-compose up -d
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

Interactive API documentation will be available at:
- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

---

## 📊 Benchmarking & Evaluation

- **Stress Testing**:
  ```bash
  locust -f benchmarks/locustfile.py --host http://localhost:8000
  ```
- **Retrieval Quality Evaluation**:
  ```bash
  python benchmarks/evaluate_retrieval.py
  ```
