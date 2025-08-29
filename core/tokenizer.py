import tiktoken

DEFAULT_MODEL = "gpt-4o-mini"

def tokenize_text(text: str, model: str = DEFAULT_MODEL):
    """
    Tokenize text and return tokens + token count
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return {
        "tokens": tokens,              # 🔹 actual tokens (list of ints)
        "token_count": len(tokens)     # 🔹 total number of tokens
    }

def estimate_cost(token_count: int, rate_per_1k: float = 0.0015):
    """
    Estimate cost in USD given token count.
    Default: gpt-4o-mini input rate $0.0015 / 1K tokens
    """
    return round((token_count / 1000) * rate_per_1k, 6)
