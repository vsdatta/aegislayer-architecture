# Hugging Face Space Metadata Guide

Use these metadata values for AegisLayer Static Spaces unless a specific Space requires an explicitly documented variation.

## Required Fields

- `title`: descriptive Space name prefixed with `AegisLayer`.
- `emoji`: one clear, stable emoji matching the Space purpose.
- `colorFrom`: one of `green`, `blue`, `yellow`, `orange`, `red`, `gray`, or `indigo` as defined in the portfolio manifest.
- `colorTo`: complementary gradient endpoint chosen from the same approved palette.
- `sdk`: `static`.
- `app_file`: `index.html`.
- `pinned`: `true` only for the organization-home Space or explicitly designated showcase Spaces.
- `license`: `apache-2.0`.
- `tags`: only accurate discoverability tags from the approved list.
- `short_description`: concise factual statement under 160 characters.

## Approved Discoverability Tags

- `ai-governance`
- `ai-security`
- `agentic-ai`
- `trustworthy-ai`
- `responsible-ai`
- `zero-trust`
- `runtime-security`
- `human-in-the-loop`
- `llm-security`
- `autonomous-agents`
- `cybersecurity`
- `governance`
- `explainability`
- `auditability`

## Title and Summary Rules

- Keep the title factual and tied to the actual Space function.
- Avoid claims of live enforcement, benchmarks, adoption, rankings, or certification.
- Use `short_description` to describe the artifact, not to market it.

## Example Metadata

```yaml
---
title: AegisLayer Policy Playground
emoji: 📜
colorFrom: yellow
colorTo: red
sdk: static
app_file: index.html
pinned: false
license: apache-2.0
tags:
  - ai-governance
  - responsible-ai
  - human-in-the-loop
  - governance
  - explainability
short_description: Deterministic policy scenarios for allow, deny, approval, and escalation outcomes.
---
```
