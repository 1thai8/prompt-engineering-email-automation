import json
import openai
from pathlib import Path

"""
This script loads test cases and sends them to the selected LLM using prompt-v1 or prompt-v2.
You can run it locally after installing OpenAI's Python SDK.

Usage:
python tests/run_tests.py --version v2
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--version", default="v2", help="Prompt version: v1 or v2")
args = parser.parse_args()

# Load test cases
test_cases_path = Path("tests/test-cases.json")
with open(test_cases_path, "r", encoding="utf-8") as f:
    test_cases = json.load(f)

# Load prompt
prompt_path = Path(f"prompts/prompt-{args.version}.txt")
with open(prompt_path, "r", encoding="utf-8") as f:
    prompt_template = f.read()

print(f"Running tests for prompt version: {args.version}")
print("-" * 50)

for case in test_cases:
    print(f"Test case: {case['id']} — {case['description']}")

    # Prepare input text
    constraints_json = json.dumps(case["constraints"], indent=2)
    filled_prompt = prompt_template.replace("{thread_text}", case["thread_text"]) \
                                   .replace("{constraints_json}", constraints_json) \
                                   .replace("{tone}", case["constraints"]["tone"]) \
                                   .replace("{word_limit}", str(case["constraints"]["word_limit"])) \
                                   .replace("{facts}", case["constraints"]["facts"])

    # Send to model (replace with your key)
    response = openai.responses.create(
        model="gpt-4.1-mini",
        input=filled_prompt
    )

    output = response.output_text
    print("Model output:")
    print(output)
    print("-" * 50)
