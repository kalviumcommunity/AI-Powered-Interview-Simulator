# multi_shot_test.py

"""
Demonstration of multi-shot (few-shot) prompting.
We include two examples in the prompt, then a final question.
"""

def get_multi_shot_prompt():
    with open("prompts/multi_shot_prompt.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    prompt = get_multi_shot_prompt()
    print("Multi-Shot Prompt Example:\n")
    print(prompt)
