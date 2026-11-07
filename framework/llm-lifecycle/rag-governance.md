# RAG Governance Standards

## Overview

Retrieval-Augmented Generation (RAG) systems ground LLM outputs in organizational data. This reduces hallucination but introduces new governance requirements: the quality, access controls, and provenance of retrieved documents directly determine the accuracy and compliance of generated outputs.

A RAG system is only as trustworthy as its retrieval pipeline. This document defines governance standards for RAG architectures in enterprise environments.

---

## RAG-Specific Risk Areas

### 1. Document Quality and Currency

**Risk:** Outdated, incorrect, or incomplete documents in the retrieval corpus produce grounded-but-wrong outputs. The LLM faithfully synthesizes bad source material.

**Controls:**
- Document freshness policy: define maximum age for each document category
- Automated staleness detection: flag documents not reviewed within defined period
- Source authority: each document linked to an accountable owner
- Version control: only the latest approved version is indexed

### 2. Access Control Leakage

**Risk:** The RAG system retrieves documents that the end user is not authorized to access, effectively bypassing document-level access controls through the LLM's response.

**Controls:**
- Row-level / document-level access control enforcement at retrieval time
- User permission context passed to the retrieval layer
- Post-retrieval access validation before documents enter the LLM context
- Access control testing: verify that restricted documents are not retrievable by unauthorized users

**Requirement (DE-008):** at every tier, where sources carry access restrictions, retrieval enforces the requesting user's source permissions at query time.
- Document-level access control lists are carried from each source system into the index with every chunk, and kept in step when source permissions change.
- The retrieval layer filters on the requesting user's identity and entitlements before any document enters the model's context. Filtering the answer afterwards is not enough.
- No cross-tenant or cross-entitlement retrieval: a user never receives content from a document they could not open in the source system.
- When an agent retrieves on a user's behalf, the user's permissions apply, narrowed by the agent's own ([delegation](agent-identity-and-tool-governance.md#2-delegation)). The agent's service identity does not widen what the user can see.
- Test before deployment with identities that hold different entitlements, and re-test on any change to sources, the index, retrieval logic or the identity integration.

### 3. Data Poisoning

**Risk:** Adversarial or low-quality content is ingested into the document store, manipulating RAG outputs.

**Controls:**
- Ingestion validation: all documents reviewed or from approved sources before indexing
- Content integrity checks: hash-based verification for indexed documents
- Source whitelisting: only approved data sources feed the retrieval corpus
- Anomaly detection: monitor for unusual patterns in newly indexed content

### 4. Context Window Pollution

**Risk:** Retrieved documents contain content that manipulates the LLM's behavior (indirect prompt injection) or introduces irrelevant noise that degrades output quality.

**Controls:**
- Input sanitization on retrieved content before it enters the LLM context
- Relevance scoring thresholds: discard low-relevance retrievals
- Maximum context budget: limit the number of retrieved chunks to prevent context dilution
- Separate retrieval context from system instructions in the prompt architecture

### 5. Attribution and Provenance

**Risk:** The LLM generates a response based on retrieved documents, but the user cannot verify which sources informed the answer. This creates audit and accountability gaps.

**Controls:**
- Mandatory source attribution: every RAG response includes references to retrieved documents
- Chunk-level provenance: track which specific chunks were used to generate each part of the response
- Audit trail: log retrieved documents, relevance scores, and generated response for every query

---

## Retrieval Quality Standards

### Chunking Governance

| Standard | Requirement |
|----------|-------------|
| Chunking strategy | Documented and justified for each document type |
| Chunk size | Defined with rationale; tested for retrieval quality impact |
| Overlap | Defined to prevent information loss at chunk boundaries |
| Metadata preservation | Document metadata (title, section, date, author, classification) retained in chunks |
| Chunk integrity | No chunks that split mid-sentence or lose semantic meaning |

### Embedding and Indexing

| Standard | Requirement |
|----------|-------------|
| Embedding model | Selected and validated per [model-selection.md](model-selection.md) criteria |
| Index freshness | Re-indexing cadence defined; triggered by document updates |
| Index integrity | Periodic validation that index matches source documents |
| Embedding drift | Monitor for embedding model changes that affect retrieval quality |

### Retrieval Evaluation

Tiered thresholds for precision@5 and faithfulness, their definitions, and RAG suite sizes are set in [evaluation-governance.md](evaluation-governance.md#threshold-definitions-by-tier). The values below restate them; the other metrics are supporting diagnostics.

| Metric | Description | Minimum Threshold |
|--------|-------------|-------------------|
| Recall@k | Proportion of relevant documents retrieved in top k | Use case specific; ≥ 0.8 recommended |
| Precision@5 | Proportion of the top 5 retrieved chunks that are relevant | T1 ≥ 85%, T2 ≥ 80%, T3 ≥ 75% ([evaluation-governance](evaluation-governance.md#threshold-definitions-by-tier)) |
| MRR | Mean Reciprocal Rank of first relevant document | ≥ 0.7 |
| Context relevance | LLM-judged relevance of retrieved context to query | ≥ 0.75 |
| Faithfulness | Average share of claims in the answer supported by retrieved context | T1 ≥ 90%, T2 ≥ 85%, T3 ≥ 80%, T4 ≥ 75% ([evaluation-governance](evaluation-governance.md#threshold-definitions-by-tier)) |
| Answer relevance | Generated answer addresses the user's query | ≥ 0.85 |

Evaluation must be performed:
- Before initial deployment (on representative test set)
- After any change to chunking strategy, embedding model, or retrieval parameters
- On a scheduled basis per [evaluation-governance.md](evaluation-governance.md#production-evaluation): weekly (T1), monthly (T2), quarterly (T3); recommended for T4
- When monitoring detects quality degradation

---

## Document Lifecycle in RAG

### Ingestion

1. Document source approved and authorized
2. Document classified per data classification policy
3. Access control metadata attached
4. Document processed (chunked, embedded, indexed)
5. Ingestion logged with provenance data

### Updates

1. Updated document replaces previous version in the index
2. Stale chunks from previous version removed
3. Change logged with old/new version references
4. If material change, trigger re-evaluation of RAG quality metrics

### Removal

1. Document owner requests removal or document expires
2. All chunks removed from index
3. Cached retrievals referencing removed document invalidated
4. Removal logged for audit trail

---

## Monitoring Requirements

### Real-Time Monitoring

| Metric | Alert Threshold |
|--------|----------------|
| Retrieval latency (p95) | Use case SLA |
| Empty retrieval rate | > 10% of queries return no relevant documents |
| Low-confidence retrieval rate | > 20% of queries have top result below relevance threshold |

### Periodic Review

| Metric | Frequency | Action |
|--------|-----------|--------|
| Retrieval quality (Recall/Precision) | Weekly (T1), Monthly (T2), Quarterly (T3); T4 recommended | Re-evaluate on updated test set |
| Faithfulness score | Per production evaluation cadence in [evaluation-governance.md](evaluation-governance.md#production-evaluation) | Investigate and remediate degradation |
| Document corpus freshness | Weekly | Flag stale documents for review |
| Access control compliance | Monthly | Audit retrieval results against user permissions |
| Index size and growth | Monthly | Capacity planning; prune irrelevant content |

---

## Multi-Tenant RAG

For organizations with multiple business units sharing a RAG platform:

| Requirement | Description |
|-------------|-------------|
| Data isolation | Tenant documents strictly isolated at storage and retrieval layers |
| Query isolation | One tenant's queries cannot retrieve another tenant's documents |
| Index separation | Separate vector indices per tenant, or strict metadata filtering with validation |
| Access audit | Regular verification that tenant boundaries are enforced |
| Cost attribution | Token and compute costs attributed to the originating tenant |
