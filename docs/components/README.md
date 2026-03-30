# Reusable Components

> Building systems, not just projects. This is a registry of the underlying "LEGO bricks" that power your portfolio.

## Registry

*   **RAG Pipeline**: Advanced semantic retrieval using hybrid search.
*   **Memory Module**: LangGraph-powered long-term conversational persistence.
*   **Eval Framework**: Standardized metrics for AI output quality.
*   **Logging System**: Observability layer for token and latency tracking.
*   **Prompt Templates**: Versioned, reusable system instructions.

---

## Component Deep Dive

### RAG Pipeline
*   **Used In**: `ai-knowledge-os`, `enterprise-search-ai`, `internal-knowledge-ai`
*   **Tech**: LangChain + Supabase pgvector
*   **Key Insight**: Hybrid search (Lexical + Semantic) is ~15% more accurate than semantic-only for technical docs.

### Memory Module
*   **Used In**: `ai-memory-layer`, `ai-onboarding-agent`
*   **Tech**: Redis for temporary, pgvector for long-term metadata extraction.
*   **Key Insight**: Summarizing old context into high-level "user traits" is more token-efficient than raw message history.

### Prompt Templates
*   **Used In**: `prompt-versioning-system`, `ux-copy-ai`, `ai-prd-system`
*   **Tech**: YAML-based versioned template files.
*   **Key Insight**: Few-shot examples in system prompts reduce hallucination by ~20%.
