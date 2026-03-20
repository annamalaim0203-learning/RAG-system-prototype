from openai import OpenAI
from config import CHAT_MODEL
from retrieve import retrieve

client = OpenAI()

SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "Answer ONLY from the provided context. "
    "If the answer is not in the context, say: I don't know."
)

def answer_question(user_query: str):
    docs, metas, dists = retrieve(user_query, candidate_k=20, top_k=5)
    context = "\n\n".join(docs)

    user_prompt = f"""Context:
{context}

Question:
{user_query}
"""

    resp = client.responses.create(
        model=CHAT_MODEL,
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    print("\n=== Answer ===")
    print(resp.output_text)

    print("\n=== Sources ===")
    for i, m in enumerate(metas, 1):
        print(f"{i}. source={m.get('source')} page={m.get('page')} distance={dists[i-1]:.4f}")

if __name__ == "__main__":
    q = "How do I reset my password?"
    answer_question(q)
