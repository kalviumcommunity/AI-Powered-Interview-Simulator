# frontend/streamlit_app.py
import streamlit as st
import pandas as pd
import textwrap
import sys
from pathlib import Path

# import core.tokenizer
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))
from core.tokenizer import tokenize_text, estimate_cost

st.set_page_config(page_title="Token Counter", page_icon="🧩", layout="centered")
st.title("🧩 Token Counter Tool")

st.caption("Paste an interview answer below to see how an LLM tokenizes it.")

model = st.selectbox(
    "Choose model encoding",
    ["gpt-4o-mini", "gpt-4o", "gpt-4.1", "gpt-3.5-turbo", "text-embedding-3-large"],
    index=0,
)

text = st.text_area(
    "Your Answer",
    height=180,
    placeholder="Type your interview answer here...",
)

col1, col2 = st.columns(2)
with col1:
    go = st.button("Count Tokens")
with col2:
    sample = st.button("Load Sample")

if sample:
    text = "I implemented a REST API using FastAPI, documented endpoints with OpenAPI, and secured it with JWT auth."

if go:
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        result = tokenize_text(text, model=model)
        token_count = result["token_count"]
        st.success(f"Token Count: {token_count}")
        st.info(f"Estimated Cost: ${estimate_cost(token_count)}")

        with st.expander("🔎 Tokens (strings)"):
            joined = " | ".join(result["token_strings"])
            st.code(textwrap.fill(joined, width=100))

        with st.expander("🔢 Token IDs"):
            st.code(result["token_ids"])

        df = pd.DataFrame({
            "Index": list(range(len(result["token_strings"]))),
            "Token String": result["token_strings"],
            "Token ID": result["token_ids"],
        })
        st.dataframe(df, use_container_width=True)
