# user_prompt_template.py

def create_user_prompt(role, answer=""):
    """
    Generates the user prompt to send to the LLM.
    If 'answer' is empty, we are starting the interview.
    If not, we are asking the model to evaluate the user's answer.
    """
    if answer.strip() == "":
        return f"User: Start a mock interview for the role of {role}."
    else:
        return f"User Answer: {answer}\nPlease evaluate the above answer."
