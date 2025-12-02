# Prompt Engineering — Email Automation

## Overview
This repository contains prompt engineering work focused on automating email tasks (summaries, reply drafting, triage). It demonstrates iterative development (v1 → v2), test cases, metrics, and rationale — suitable for portfolio and recruiters.

# Structure
- `prompts/` - prompt versions (prompt-v1.txt, prompt-v2.txt)
- `tests/` - test cases used to evaluate prompts (JSON)
- `metrics/` - metrics and evaluation templates
- `CHANGELOG.md` - history of improvements and reasoning
- `INSIGHTS.md` - technical decisions and notes

# How to evaluate locally (manual)
1. Use any LLM playground (OpenAI, Anthropic, etc.) or local LLM.
2. Load `prompts/prompt-v1.txt` and run the test inputs from `tests/test-cases.json`.
3. Save outputs and record metric values in `metrics/metrics-template.md`.

# How to present to recruiters 
- Show before/after examples (v1 vs v2).
- Include a short video/GIF of prompt in action or a link to outputs saved in `examples/`.
- Use commit history to explain changes.

