# Failures

> Most builders hide their failures. Seniors document them, fix them, and learn what not to do next time. This is your elite-level signal.

## Failure Log

### Project: vector-db-benchmark
### Date: 2026-03-20
### What failed:
Benchmarking results were wildly inconsistent across different datasets.

**Why:**
Incorrectly assumed a single vector embedding model (OpenAI ada-002) was the baseline for all tests. Failed to account for local HNSWD optimization settings in ChromaDB vs. Supabase.

**What I learned:**
Benchmarking is a surface-level activity unless you control for the underlying indexing algorithms and hardware resources. Never trust a "benchmark" that doesn't explicitly define its infrastructure and model versions.

---

### Project: multi-agent-orchestrator
### Date: 2026-03-25
### What failed:
Recursive loops in agent communication caused token cost to spike ($42 in 10 minutes).

**Why:**
No recursion depth limit or "circuit breaker" was implemented in the agentic loop. Agents were caught in a feedback loop asking each other for clarification on an impossible task.

**What I learned:**
In agentic systems, **Guardrails are non-negotiable**. Every autonomous loop must have a hard stop on: 1) Max steps 2) Max tokens 3) Max cost.

---

## Format

### Project:
### What failed:
### Why:
### What I learned:
