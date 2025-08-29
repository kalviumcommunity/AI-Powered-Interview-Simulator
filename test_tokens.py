from core.tokenizer import tokenize_text, estimate_cost

def demo_token_count():
    sample_texts = [
        "I am preparing for an AI interview.",
        "Explain the concept of REST API in simple terms.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for text in sample_texts:
        result = tokenize_text(text)
        cost = estimate_cost(result["token_count"])

        # 🔹 log output in console
        print("=" * 60)
        print(f"Input Text      : {text}")
        print(f"Tokens          : {result['tokens']}")
        print(f"Token Count     : {result['token_count']}")
        print(f"Estimated Cost  : ${cost}")
        print("=" * 60 + "\n")

if __name__ == "__main__":
    demo_token_count()
