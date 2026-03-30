# 🏗️ Architectural Decision Records (ADR)

> **"Architecture is about the important stuff. Whatever that is."** — Ralph Johnson.
> This repository uses ADRs to document the "Why" behind every major technical and product choice.

## ADR Index

| ID | Title | Date | Status |
| -- | ----- | ---- | ------ |
| 001 | [Use Supabase Vector (pgvector) for Retrieval](#adr-001-use-supabase-vector-pgvector-for-retrieval) | 2026-03-30 | ✅ Accepted |

---

## ADR 001: Use Supabase Vector (pgvector) for Retrieval

### Status
Accepted (2026-03-30)

### Context
The AI Knowledge OS and other Tier 1 projects require a reliable, scalable vector database for semantic search and RAG retrieval. We need a solution that balances performance with architectural simplicity.

### Options Considered
*   **Pinecone**: Specialized vector database. High performance but introduces a new vendor and separate billing/auth.
*   **Supabase (pgvector)**: Integrated with PostgreSQL. Allows relational + vector queries in one database.
*   **Weaviate**: Open-source, high-performance, but higher ops overhead for a solo lab.

### Decision
We will use **Supabase (pgvector)**.

### Rationale
- **Architectural Simplification**: By keeping relational data and vector embeddings in the same database, we avoid complex synchronization logic between disjoint systems.
- **Cost/Ops Efficiency**: Leveraging our existing Supabase instance reduces cognitive load and operational overhead.
- **Query Flexibility**: We can perform "Hybrid Search" (filtering by user meta-data AND semantic content) in a single SQL query.

### Consequences
*   **Positive**: Faster development cycle; simplified authentication and row-level security (RLS).
*   **Negative**: We are tied to the PostgreSQL ecosystem for vector operations.
*   **Neutral**: Performance is slightly lower than Pinecone at "million-scale," which is acceptable for these project tiers.

---

## [NEW] ADR Template

### Status
(Proposed / Accepted / Deprecated)

### Context
What is the issue that we're seeing?

### Decision
What is the change that we're proposing and/or making?

### Rationale
Why is this the best choice?

### Consequences
What becomes easier or more difficult to do and any risks introduced?
