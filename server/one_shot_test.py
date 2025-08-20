# one_shot_test.py

"""
Demonstration of one-shot prompting:
We include one example + then ask a new question for the model to answer.
"""

def get_one_shot_prompt():
    with open("prompts/one_shot_prompt.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    prompt = get_one_shot_prompt()
    print("One-Shot Prompt Example:\n")
    print(prompt)
    # In real usage, we will send this as prompt to GPT-4 or Gemini.
