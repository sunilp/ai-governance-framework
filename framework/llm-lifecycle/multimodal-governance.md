# Multimodal AI Governance

## Overview

Multimodal AI systems process or generate content across modalities — images, audio, video, or combinations. Each modality introduces governance requirements that text-only standards do not address: biometric consent, synthetic media labeling, content safety for visual/audio content, and cross-modal consistency.

This document defines lifecycle governance standards for multimodal systems. For risk classification, see [multimodal-risk-matrix.md](../risk-classification/multimodal-risk-matrix.md). For text-only GenAI standards, see the other documents in this directory.

---

## Input Governance

### Image Inputs

| Risk | Required Control | Tier |
|------|-----------------|:---:|
| CSAM / child exploitation content | Mandatory content safety classifier (PhotoDNA, CSAM detection API, or equivalent); block and report | All |
| Violence / explicit content | Content safety classifier; block or flag per policy | T1/T2 mandatory; T3/T4 recommended |
| PII in images (faces, documents, license plates) | PII detection and redaction before processing; consent verification | T1/T2 |
| Biometric data (faces for identification) | Explicit consent; GDPR Article 9 DPIA; legal basis documented | T1 mandatory |
| Medical / diagnostic imagery | Clinical validation requirements; regulatory compliance (MDR, FDA) | T1 mandatory |

### Audio Inputs

| Risk | Required Control | Tier |
|------|-----------------|:---:|
| Speaker identification without consent | Consent verification before processing; disclosure that audio is being analyzed | T1/T2 |
| Recording of conversations | Comply with recording consent laws (one-party vs. all-party jurisdictions) | All |
| Accent / dialect bias | Accuracy testing across accent groups as part of evaluation | T1/T2 |
| Sensitive spoken content | Content classification; appropriate handling per data classification policy | T1/T2 |

### Video Inputs

| Risk | Required Control | Tier |
|------|-----------------|:---:|
| Surveillance-grade analysis | Legal basis required; DPIA for GDPR; proportionality assessment | T1 mandatory |
| Behavioral analysis | Explicit purpose limitation; no repurposing without re-assessment | T1/T2 |
| PII in video (faces, vehicle plates, locations) | PII detection; anonymization where identity is not required | T1/T2 |
| Content moderation (violence, explicit material) | Content safety classification; block or flag per policy | All |

### All Modalities

- Classify input data per existing data classification policy before processing
- Apply data residency requirements per [data-residency-llm.md](../compliance/data-residency-llm.md) — biometric data has additional residency restrictions under GDPR
- Document which modalities each system processes in the model card

---

## Output Governance

### Synthetic Media Labeling

| Output Type | Labeling Requirement | Standard | Tier |
|------------|---------------------|----------|:---:|
| Generated images | Machine-readable provenance metadata (C2PA / Content Credentials) | C2PA 1.4+ | T1/T2 mandatory |
| Generated images for external distribution | Visible watermark in addition to metadata | Organizational standard | T1 mandatory |
| Generated audio | Provenance metadata; disclosure of AI generation | C2PA where supported | T1/T2 |
| Synthetic voice (text-to-speech) | Disclosure that voice is AI-generated when presented to end users | EU AI Act Article 50 | All customer-facing |
| Generated video | Mandatory disclosure per EU AI Act Article 50; machine-readable metadata | C2PA | T1/T2 |
| Modified images/video | Disclosure of AI modification; original preserved for audit | C2PA | T1/T2 |

### Content Safety on Outputs

| Check | Description | Tier |
|-------|-------------|:---:|
| Generated image safety | Run safety classifier on all generated images before delivery | All |
| Deepfake detection | Run deepfake detection on all generated face imagery | T1 mandatory |
| Copyright similarity | Check generated imagery for similarity to known copyrighted works (for T1) | T1 |
| Generated audio safety | Verify no impersonation of real individuals without consent | T1/T2 |
| Cross-modal consistency | Verify text descriptions and generated visuals are consistent | T1/T2 |

### Downstream Usage Controls

- Document permitted downstream uses of generated content in the model card
- Prohibit use of generated content for: identity fraud, non-consensual intimate imagery, disinformation
- Implement technical controls where feasible (watermarking, access controls, usage logging)

---

## Evaluation Standards

### Modality-Specific Evaluation Suites

| Modality | Evaluation Type | Minimum Suite Size by Tier |
|----------|----------------|:---:|
| Vision — understanding | Object recognition accuracy, scene understanding, OCR accuracy | T1: 200, T2: 100, T3: 50, T4: 20 |
| Vision — generation | Image quality, prompt fidelity, safety (no harmful content), diversity | T1: 200, T2: 100, T3: 50, T4: 20 |
| Audio — understanding | Transcription accuracy (WER), speaker diarization, language detection | T1: 200, T2: 100, T3: 50, T4: 20 |
| Audio — generation | Naturalness (MOS), intelligibility, safety, speaker similarity (TTS) | T1: 200, T2: 100, T3: 50, T4: 20 |
| Video — understanding | Action recognition, temporal understanding, scene consistency | T1: 200, T2: 100, T3: 50, T4: 20 |
| Cross-modal consistency | Text-image alignment, audio-visual sync, multimodal reasoning | T1: 100, T2: 50, T3: 25 |

### Demographic Parity Testing

For vision and audio systems at T1/T2:

| Modality | Parity Dimension | Test Methodology |
|----------|-----------------|-----------------|
| Vision (understanding) | Accuracy across skin tones (Monk Skin Tone Scale) | Test recognition accuracy per skin tone group; max disparity < 5% |
| Vision (understanding) | Accuracy across genders, ages | Balanced test set; report per-group metrics |
| Vision (generation) | Diversity of generated content | Audit generated imagery for demographic representation; test for stereotypical associations |
| Audio | Accuracy across accents and dialects | Test WER per accent group; max disparity < 10% |
| Audio | Accuracy across genders and ages | Balanced test set; report per-group metrics |

---

## Responsible AI for Multimodal Systems

### Fairness

- **Image recognition bias**: test across Monk Skin Tone Scale (10 categories); report performance per category
- **Generated imagery bias**: audit for stereotypical associations (e.g., profession + gender, activity + ethnicity); test with counterfactual prompts
- **Voice bias**: test speech recognition and generation quality across accents, genders, and age groups
- **Representation**: generated content should reflect demographic diversity unless explicitly constrained by use case

### Accessibility

| Requirement | Description | Tier |
|------------|-------------|:---:|
| Alt-text generation | Vision systems generating descriptions must produce accurate alt-text | T1/T2 |
| Caption generation | Audio/video systems must support captioning for hearing-impaired users | All customer-facing |
| Audio descriptions | Video systems should support audio descriptions for vision-impaired users | T1 |
| Assistive technology testing | Test with screen readers and other assistive technologies | All customer-facing |

---

## Production Monitoring

| Metric | Description | Cadence |
|--------|-------------|---------|
| Output modality distribution | Track what types of content the system is producing over time | Daily |
| Content safety classifier metrics | False positive/negative rates on safety classifiers per modality | Weekly |
| Modality-specific drift | Quality metric trends per modality (accuracy, safety scores, user satisfaction) | Weekly |
| Cross-modal consistency score | Agreement between modalities when system produces multi-modal output | Weekly |
| Demographic parity metrics | Per-group performance metrics for vision and audio systems | Monthly |
| Synthetic media labeling compliance | % of generated content with proper provenance metadata | Monthly |

---

## Integration with Existing Governance

- Risk classification: use [multimodal-risk-matrix.md](../risk-classification/multimodal-risk-matrix.md) alongside [genai-risk-matrix.md](../risk-classification/genai-risk-matrix.md)
- Deployment gates: multimodal evaluations are additional gates on top of [deployment-gates.md](deployment-gates.md)
- Incident response: extend [GenAI incident taxonomy](../../templates/incident-report-genai.md) with modality-specific incident types (deepfake generation, content safety failure, biometric privacy breach)
- Model card: document modalities processed/generated, safety classifiers deployed, labeling standards applied
