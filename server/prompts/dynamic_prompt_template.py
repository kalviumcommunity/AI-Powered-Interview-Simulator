# dynamic_prompt_template.py

def generate_prompt(role, question, answer=None):
    """
    Dynamically generates a prompt for the LLM based on input.
    If answer is None, we ask the question.
    If answer exists, we evaluate the answer.
    """

    if answer is None:
        return f"You are an interviewer for the role of {role}.\nAsk this question to the user: {question}"
    else:
        return (
            f"You are an interviewer for the role of {role}.\n"
            f"Interview Question: {question}\n"
            f"User Answer: {answer}\n"
            f"Evaluate the answer in JSON format."
        )
