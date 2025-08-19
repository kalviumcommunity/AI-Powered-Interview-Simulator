from prompts.user_prompt_template import create_user_prompt

role = "Backend Developer"

# 1) Start interview
start_prompt = create_user_prompt(role)
print("System Prompt (from file):")
with open("prompts/system_prompt.txt") as f:
    print(f.read())

print("\nUser Prompt:")
print(start_prompt)

# 2) After user answer
answer_prompt = create_user_prompt(role, answer="A closure is a function having access to its outer scope even after the outer function has finished executing.")
print("\nEvaluation User Prompt:")
print(answer_prompt)
