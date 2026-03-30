# Project Template (v2)

## 0. Project Identity

* Name:
* Category: (System / Product / Experiment / Teardown / Meta)
* Depth: (Shallow / Deep)
* Narrative Tag: (Builder / Systems / PM / Hybrid)
* Tier: (1 / 2 / 3)
* Pattern: (RAG / Agent / Eval loop / etc.)

---

## 1. Problem Definition

* What exact problem exists?
* Who faces it?
* Why is it painful today?
* Why hasn’t it been solved properly?

---

## 2. Why AI?

* What part requires AI?
* Why can’t traditional systems solve this well?
* What type of AI fits best? (LLM / RAG / Agent / Hybrid)

---

## 3. User Journey

Step-by-step:

1. Entry point
2. Interaction
3. Output
4. Feedback loop

---

## 4. Solution Design

### Core Components:

* Input Layer
* Processing Layer (LLM / RAG / Agents)
* Memory Layer (if applicable)
* Output Layer
* Feedback / Learning Layer

---

## 5. System Architecture

* Data flow (step-by-step)
* Storage (vector DB, DB)
* APIs used
* Latency considerations

### System Diagram
![System Architecture Diagram](link-to-diagram-image)
*(Use Excalidraw / Whimsical / Mermaid)*

---

## 6. Key Product Decisions

* Why this UX?
* Why this workflow?
* What alternatives were rejected?

> Refer to [DECISION_LOG.md](../docs/adr/README.md) for full context on these choices.

---

## 7. Tradeoffs

| Decision | Alternative | Why chosen | Risk |
| -------- | ----------- | ---------- | ---- |

---

## 8. Failure Modes

* Hallucinations
* Incorrect retrieval
* Latency issues
* Cost explosion

---

## 9. Evaluation Strategy

* How do we measure success?
* Metrics:

  * Accuracy
  * Relevance
  * Latency
  * Cost

> See [EVALS.md](../docs/evals/README.md) for detailed test cases and results.

---

## 10. Scaling Thought Experiment

If this had:

* 10K users
* 100K users
* 1M users

What breaks?

---

## 11. Future Improvements

* Short-term
* Long-term
* “If I had a team”

---

## 12. Demo

* Screenshots
* Loom
* Live link
