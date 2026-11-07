# Multimodal AI Risk Classification Matrix

## Overview

Multimodal AI systems — those that process or generate images, audio, video, or combinations of modalities — introduce risk categories that text-only GenAI frameworks do not cover. Misidentified medical imagery, cloned voices, and synthetic video each carry distinct harm profiles that require dedicated assessment.

This matrix extends the existing four-tier risk classification (T1–T4) with modality-specific risk dimensions. Use it alongside the existing [risk-matrix.md](risk-matrix.md) and [genai-risk-matrix.md](genai-risk-matrix.md). The highest tier across all applicable matrices applies to the combined system.

---

## Modality-Specific Risk Dimensions

### Dimension 1: Vision Risk

Risks arising from AI systems that process or generate images.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Misidentification causes safety, legal, or financial harm; synthetic imagery enables fraud or abuse | Medical diagnostic imaging, identity verification, deepfake generation for fraud |
| High | Visual misinterpretation influences consequential decisions; generated imagery requires attribution | Insurance claim image analysis, document OCR for compliance, marketing image generation |
| Medium | Visual processing errors cause operational inefficiency | Product categorization, internal document scanning, presentation generation |
| Low | Visual output is advisory or creative with minimal consequence | Design brainstorming, internal mood boards, data visualization |

### Dimension 2: Audio Risk

Risks arising from AI systems that process or generate audio content.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Voice cloning enables impersonation or fraud; transcription errors in regulated contexts | Voice authentication bypass, synthetic voice for social engineering, legal/compliance transcription |
| High | Audio processing errors affect business decisions; speaker identification without explicit consent | Meeting transcription for action items, call center analytics, earnings call analysis |
| Medium | Transcription or synthesis errors cause rework | Internal meeting notes, podcast generation, language translation |
| Low | Audio output is non-consequential | Music generation, notification sounds, internal voice memos |

### Dimension 3: Video Risk

Risks arising from AI systems that process or generate video content.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Video manipulation or synthesis enables fraud, surveillance, or abuse; real-time deepfake | KYC video verification, surveillance-grade behavioral analysis, real-time video synthesis |
| High | Video analysis errors influence decisions; temporal manipulation | Security footage analysis, customer behavior tracking, training video generation |
| Medium | Video processing errors cause operational inefficiency | Meeting recording summarization, internal training content, product demos |
| Low | Video output is advisory or creative | Marketing concept videos, internal presentations |

### Dimension 4: Cross-Modal Consistency Risk

Risks arising when AI systems operate across multiple modalities simultaneously.

| Level | Description | Examples |
|-------|-------------|----------|
| Critical | Cross-modal inconsistency causes harm (text says one thing, image shows another) | Medical report + diagnostic image generation, financial report + chart generation |
| High | Modal outputs are consumed together; inconsistency misleads | Research summaries with generated visualizations, automated presentations |
| Medium | Modalities are loosely coupled; inconsistency causes confusion | Document summarization with extracted images, meeting notes with audio clips |
| Low | Modalities are independent | Separate text and image generation for different purposes |

---

## Tier Determination

Score each dimension Critical (4), High (3), Medium (2) or Low (1). The highest-scoring dimension sets the tier, using the same rule as the [GenAI risk matrix](genai-risk-matrix.md#risk-tier-determination-for-genai): any Critical gives T1; otherwise any High gives T2; otherwise any Medium gives T3; all Low gives T4. The aggregate score is recorded for context only and does not set the tier. For example, real-time video analysis in surveillance contexts scores Critical on Video Risk, so it is T1.

### Tier Override Rules

This is the canonical override list, also used in [genai-risk-matrix.md](genai-risk-matrix.md#tier-override-rules) and [agentic-ai-risk.md](agentic-ai-risk.md). Overrides can raise the tier, never lower it.

**Automatic T1:**

1. Makes or directly influences regulated decisions (credit, insurance underwriting or pricing, AML/sanctions, employment).
2. Generates customer-facing content delivered without per-output human review.
3. Processes customer personal data through an external LLM API without **all** of these safeguards: zero data retention by the vendor, a regional endpoint that meets data residency requirements, a signed DPA, and PII redaction or minimisation before the call. (With all four safeguards in place: minimum T2, and normal scoring decides.)
4. Agentic behaviour with write access to production systems or data stores, or with authority to move money, communicate with customers, or change identity and access.
5. Biometric identification or categorisation; synthetic media that can depict real people (deepfake-capable); voice cloning; medical imagery.

**Minimum T2:**

6. Any agentic system, including read-only tool use, and any multi-agent system.
7. Synthetic media generation not covered by item 5.
8. Customer personal data through an external LLM API with all four safeguards in place.
9. Personal data in visual content.

**Emotion recognition** (inferring emotions or intentions from biometric data such as facial expressions, voice or keystrokes):
- **Workplace and education:** prohibited under EU AI Act Art. 5(1)(f), except for medical or safety reasons. Reject it at the [Step 0 prohibited-use screen](genai-risk-matrix.md#step-0-prohibited-use-screen). For example, call-centre voice analytics that infer the emotions of staff fall under the prohibition.
- **Other contexts**, such as inferring customers' emotions: treat it as biometric categorisation under item 5 (automatic T1). It is high-risk under Annex III point 1(c), and deployers must inform the people exposed to it (Art. 50(3)).

Inferring emotions from written text, such as sentiment analysis, does not use biometric data and is not emotion recognition under the Act. See the [EU AI Act mapping](../compliance/eu-ai-act-mapping.md#d-transparency-duties-art-50).

---

## Governance Requirements by Tier (Multimodal-Specific)

### T1 — Critical Multimodal Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Content safety | Mandatory classifiers for CSAM, violence, explicit content on all image/video inputs and outputs |
| Synthetic media labeling | C2PA/Content Credentials metadata on all generated media; visible watermarking for external distribution |
| Biometric compliance | GDPR Article 9 (special categories), explicit consent, DPIA completed |
| Deepfake detection | Deploy detection capability on all video/image inputs for systems processing identity |
| Cross-modal validation | Automated consistency checking between modalities |
| Evaluation | Modality-specific eval suites: 200+ test cases per modality, demographic parity testing |
| Red-teaming | Modality-specific adversarial testing (adversarial images, audio perturbation, video manipulation) |

### T2 — High Multimodal Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Content safety | Content classifiers on inputs and outputs |
| Synthetic media labeling | Machine-readable provenance metadata on all generated media |
| Evaluation | 100+ test cases per modality |
| Bias testing | Demographic parity testing for vision systems (race, gender, age) |

### T3/T4 — Medium/Low Multimodal Use Cases

| Control Area | Requirement |
|-------------|-------------|
| Content safety | Basic content filtering |
| Synthetic media labeling | Internal labeling of AI-generated content |
| Evaluation | 50 test cases (T3), pre-deployment validation (T4) |

---

## Responsible AI for Multimodal Systems

### Fairness Across Modalities

| Modality | Fairness Concern | Required Testing |
|----------|-----------------|-----------------|
| Vision | Recognition accuracy varies by skin tone, gender, age | Demographic parity analysis; test across skin tone scales (Monk, Fitzpatrick) |
| Audio | Recognition accuracy varies by accent, dialect, gender, age | Accuracy testing across accent groups, languages, genders |
| Video | Activity recognition bias (cultural, demographic) | Diverse scenario testing across demographics |
| Generated imagery | Representation bias in generated content | Audit generated output diversity; test for stereotypical associations |
| Generated audio | Voice quality and naturalness varies by language | Quality testing across target languages |

### Accessibility

- Vision systems: provide text alternatives for visual outputs
- Audio systems: provide transcription and visual alternatives
- Video systems: provide captions, audio descriptions, and text summaries
- All systems: test with assistive technologies where user-facing

---

## Integration with Existing Matrices

For systems combining text and non-text modalities (e.g., a RAG chatbot that also processes uploaded images):

1. Assess text dimensions using [genai-risk-matrix.md](genai-risk-matrix.md)
2. Assess multimodal dimensions using this matrix
3. Apply the higher tier to the combined system
4. Document the interaction between modalities in the risk assessment
