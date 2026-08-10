---
name: paper-writing
description: Draft and revise ML/CV/NLP research papers with reviewer-facing structure, paragraph flow, and evidence-backed claims. Use when writing or revising Abstract, Introduction, Related Work, Method, Experiments, or Conclusion; polishing figures/tables; checking claim-support alignment; or running pre-submission self-review.
---

# Paper Writing

Rewrite papers into reviewer-friendly, high-clarity drafts. Prioritize first-impression quality (figures/tables/layout), logical flow, and evidence-backed claims.

## Workflow

1. Clarify the paper story before sentence-level edits.
2. Load the section-specific guide from `references/` only when editing that section.
3. Rewrite paragraph-by-paragraph — one message per paragraph, message in the first sentence.
4. Run reverse outlining after each section: extract thesis → topic sentences → evidence, then verify every paragraph maps cleanly.
5. Run anti-AI style check with `references/anti-ai-style.md` — flag high-frequency terms, throat-clearing openers, punctuation overuse, structural monotony.
6. Check every major claim in Abstract/Introduction against experimental evidence.
7. Run adversarial self-review with `references/paper-review.md`.

## Principles

1. One paragraph, one message. First sentence states it.
2. Self-contained nouns — define new terms before reusing them.
3. Sentence-to-sentence flow via explicit relations (cause, contrast, consequence, refinement).
4. Visual quality is core content, not decoration — clean teaser figure, minimal-ink tables.
5. Terminology stable across the full paper.
6. If a claim cannot be supported by results, weaken or remove it.
7. Avoid AI-typical writing patterns — overused vocabulary, throat-clearing openers, em dash abuse, uniform paragraph rhythm. See `references/anti-ai-style.md`.

## Section Guides

Load only the needed file:

| Section | Reference |
|---------|-----------|
| Abstract | `references/abstract.md` |
| Introduction | `references/introduction.md` |
| Related Work | `references/related-work.md` |
| Method | `references/method.md` |
| Experiments | `references/experiments.md` |
| Conclusion | `references/conclusion.md` |
| Pre-submission review | `references/paper-review.md` |
| Anti-AI style check | `references/anti-ai-style.md` |

Each guide includes templates, sentence skeletons, and pointers to `references/examples/`.

## Output Contract

When drafting or revising, return:

1. A compact section outline (3–7 bullets).
2. Revised paragraphs with explicit roles (opening / challenge / method / advantage / evidence / limitation).
3. A self-review checklist: clarity, flow, terminology consistency, unsupported claims, missing evidence.
4. A claim-evidence map: `Claim: ... | Evidence: ... | Status: supported / needs evidence`.
