# 🧪 AI Evaluation Framework (LLM-as-a-Judge)

> **"You can't manage what you can't measure."**
> In AI systems, traditional unit tests are insufficient. This framework defines how we use advanced metrics and LLM-based evaluation to ensure system quality.

## 📐 Core Evaluation Metrics (The RAG Triad)

We prioritize the **RAG Triad** plus standard performance metrics for all Tier 1 projects:

### 1. Faithfulness (Groundedness)
-   **Definition**: Is the answer derived *only* from the retrieved context?
-   **Goal**: Zero hallucinations.
-   **Judge Prompt**: *"Does the following answer contain any information not present in the provided context blocks?"*

### 2. Answer Relevance
-   **Definition**: Does the answer actually address the user's query?
-   **Goal**: High utility and directness.
-   **Judge Prompt**: *"Rate the relevance of the answer to the user's query on a scale of 1-5."*

### 3. Context Precision
-   **Definition**: Was the retrieved context actually relevant to the query?
-   **Goal**: High-signal retrieval, low noise.
-   **Judge Prompt**: *"Rank the retrieved documents by their relevance to answering the user's specific question."*

---

## 🛠️ Tools & Methods

### Method A: Manual Benchmarking (Tier 3)
-   Comparison of raw outputs via `evals/README.md`.
-   Best for rapid prototyping and initial vibes-check.

### Method B: LLM-as-a-Judge (Tier 1 & 2)
-   Use a stronger model (e.g., GPT-4o or Claude 3.5 Sonnet) to grade the output of a smaller/faster model.
-   **Automated Scores**: Use JSON output to generate pass/fail metrics.

### Method C: RAGAS / DeepEval (Tier 1 Flagships)
-   Standardized Python frameworks for calculating the metrics above at scale.
-   **Output**: Exportable CSV/JSON reports for PR evidence.

---

## 📋 Evaluation Workflow

1.  **Define Golden Set**: Create a list of 10-20 "Perfect" Q&A pairs for the project.
2.  **Run Inference**: Generate answers for the Golden Set using the current system.
3.  **Judge Output**: Use the judge model to score based on the RAG Triad.
4.  **Analyze & Iterate**: Identify failure modes (e.g., "Retrieval failed on document X") and fix the system.
5.  **Record**: Log the final run in `docs/evals/README.md`.
