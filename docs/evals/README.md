# Evaluation

> AI systems are only as good as their metrics. This file tracks the performance of key projects against rigorous benchmarks.

## What are we measuring?

*   **Accuracy**: How correct is the output? (Ground truth comparison)
*   **Relevance**: How helpful is the output to the user's intent?
*   **Latency**: How fast is the system? (Time-to-first-token & total duration)
*   **Cost**: What is the token usage and dollar cost per interaction?

> **📘 Detailed Framework**: See our [Advanced Evaluation Framework](FRAMEWORK.md) for LLM-as-a-Judge metrics and RAG Triad scoring.

---

## Evaluation Reports

### Project: ai-knowledge-os

#### Test Cases
*   **Case 1**: Complex query across three disparate documents.
*   **Case 2**: Ambiguous query requiring clarification.
*   **Case 3**: High-volume ingestion of 50+ PDFs.

#### Results
| Case | Accuracy | Relevance | Latency | Cost (Est) |
| ---- | -------- | --------- | ------- | ---------- |
| 1    | 92%      | High      | 1.2s    | $0.004     |
| 2    | 85%      | Medium    | 0.8s    | $0.002     |
| 3    | 98%      | High      | 45s     | $0.120     |

#### Observations
*   Retrieval accuracy drops when documents have overlapping terminology.
*   Latency for cold-starts on serverless functions is a noticeable bottleneck.

#### Proposed Improvements
*   Implement hybrid search (Keyword + Semantic) to resolve terminology overlaps.
*   Add a warm-up phase or use edge-cached retrievals to reduce latency.
