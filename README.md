# Prompt Engineering — Email Automation

## Overview
This repository contains prompt engineering work focused on automating email tasks (summaries, reply drafting, triage). It demonstrates iterative development (v1 → v3), test cases, examples, and rationale — suitable for portfolio and recruiters.

## Structure
- `prompts/` — all prompt versions:
  - `prompt_v1_email_assistant.md`
  - `prompt_v2_email_assistant.md`
  - `prompt_v3_email_assistant.md`
- `tests/` — scripts and test cases:
  - `run_tests.py`
  - `test-cases.json`
- `examples/` — sample outputs from each prompt version:
  - `sample-output-v1.json`
  - `sample-output-v2.json`
  - `sample-output-v3.json`
- `README.md` — project documentation
- `metrics/` — metrics template (`metrics-template.md`)
- `CHANGELOG.md` — history of improvements
- `INSIGHTS.md` — technical decisions and notes
- `LICENSE` — license file

## How to evaluate locally
1. Open any LLM playground (OpenAI, Anthropic, etc.) or local LLM.
2. Copy a prompt from `prompts/` and fill in the input placeholders.
3. Run the prompt with test cases from `tests/test-cases.json`.
4. Save outputs in `examples/` and optionally record metrics or notes in the `notes` fields.

## How to present to recruiters
- Show prompt evolution (v1 → v2 → v3) with outputs.
- Include `examples/` to demonstrate real model outputs.
- Optional: add short video/GIF of prompt in action.
- Use commit history to highlight improvements and rationale.


