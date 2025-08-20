# chain_of_thought_test.py

"""
Demonstration of Chain-of-Thought Prompting: telling the model to think step by step.
"""

def get_cot_prompt():
    with open("prompts/chain_of_thought_prompt.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    prompt = get_cot_prompt()
    print("Chain-of-Thought Prompt:\n")
    print(prompt)
    print("\n(If we submit this to an LLM, it should show step-by-step reasoning.)")
