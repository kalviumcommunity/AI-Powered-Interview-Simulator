# evaluation_test_framework.py

import json

def load_dataset():
    with open("evaluation_dataset.json", "r") as f:
        return json.load(f)

def mock_model_answer(question):
    """
    This is a mock function. In real life, we would call GPT or Gemini API.
    """
    # Hard-coded fake answers (simulation)
    if "closure" in question.lower():
        return "A closure is a function that can access variables from its outer scope even after the function has returned."
    if "rest api" in question.lower():
        return "REST API is an architectural style that uses HTTP methods to access or modify resources in a stateless manner."
    return ""

def evaluate_answers():
    dataset = load_dataset()
    results = []
    for item in dataset:
        question = item["question"]
        expected_keywords = item["expected_keywords"]
        answer = mock_model_answer(question)

        present = 0
        for kw in expected_keywords:
            if kw.lower() in answer.lower():
                present += 1
        
        score = present / len(expected_keywords) * 10
        results.append({
            "question": question,
            "answer": answer,
            "score": score
        })
    
    return results

if __name__ == "__main__":
    results = evaluate_answers()
    for r in results:
        print("Question:", r["question"])
        print("Answer:", r["answer"])
        print("Score out of 10:", r["score"])
        print("-" * 40)
