# zero_shot_test.py

"""
This file simulates a zero-shot prompt example.
We do not give any examples to the LLM. We only send a direct question.
"""

def get_zero_shot_prompt():
    with open("prompts/zero_shot_prompt.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    prompt = get_zero_shot_prompt()
    print("Zero-Shot Prompt Example:\n")
    print(prompt)
    # In real usage, we would send this prompt to an LLM (GPT-4 or Gemini) to get an answer.
