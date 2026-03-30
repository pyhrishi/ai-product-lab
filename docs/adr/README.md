# Decision Log

> PMs are judged by decisions, not outputs. Use this log to track the "why" behind every major choice in your projects.

## Format

### Project: [Project Name]
### Date: [YYYY-MM-DD]
### Decision: [What choice did I make?]

### Context:
Why was this decision needed?

### Options Considered:
1. [Option 1]
2. [Option 2]
3. [Option 3]

### Chosen Approach:
What I picked.

### Why:
Reasoning (technical, user needs, trade-offs).

### Tradeoffs:
What I accepted as downsides.

### Outcome:
Did it work? (Updated after implementation)

### Reflection:
Would I change this later?

---

## Decisions

### Project: ai-knowledge-os
### Date: 2026-03-30
### Decision: Use Supabase Vector instead of Pinecone

**Context:**
Need a scalable, easy-to-manage vector database for the AI Knowledge OS.

**Options Considered:**
1. Pinecone (Serverless) - Best for large scale, but standalone.
2. Supabase Vector (pgvector) - Integrated with existing database.
3. Weaviate - High performance, but more complex setup.

**Chosen Approach:**
Supabase Vector (pgvector)

**Why:**
Already using Supabase for auth and relational data. Integrated vector search reduces architectural complexity and allows for complex relational + semantic queries in one go.

**Tradeoffs:**
Slightly less optimized for massive-scale vector search compared to specialized engines like Pinecone, but more than sufficient for personal/enterprise knowledge bases.

**Outcome:**
Successfully implemented; simplified data model significantly.

**Reflection:**
Correct choice for MVP/V1. Integration speed outweighed specialized performance.
