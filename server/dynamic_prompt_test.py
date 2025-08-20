# dynamic_prompt_test.py

"""
Demonstration of Dynamic Prompting
We are generating a prompt based on variables: role, question, answer
"""

from prompts.dynamic_prompt_template import generate_prompt

if __name__ == "__main__":
    role = "Frontend Developer"
    question = "What is virtual DOM?"
    
    # Case 1: Asking the question
    ask_prompt = generate_prompt(role, question)
    print("Dynamic Ask Prompt:\n", ask_prompt)

    # Case 2: Evaluating the answer
    answer = "It is a lightweight copy of the real DOM used by React to update UI efficiently."
    eval_prompt = generate_prompt(role, question, answer)
    print("\nDynamic Evaluation Prompt:\n", eval_prompt)
