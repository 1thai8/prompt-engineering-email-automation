# Metrics Template

Record metrics for each prompt version and test case.

## Suggested metrics
- **Relevance score (0-5):** how well reply answers email.
- **Conciseness (0-5):** brevity and absence of fluff.
- **Accuracy (0-5):** no hallucinations, factual correctness.
- **CTA presence (yes/no):** expected vs present.
- **Human-likeness (0-5):** naturalness of tone.

## Example entry
- prompt_version: v1
- test_case: case-001
- relevance: 4
- conciseness: 3
- accuracy: 5
- CTA_presence: no
- human_likeness: 4
- notes: "Missing explicit CTA asking to confirm address."
