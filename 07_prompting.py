import os
import requests
from importlib import import_module

retrieve_module = import_module("06_retrieve_context")
retrieve_context = retrieve_module.retrieve_context

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "openai/gpt-4o-mini")

def build_prompt(question, context_chunks):
    context_text = "\n\n".join(context_chunks)
    prompt = "Answer the question based only on the context below.\n"
    prompt += "If the answer is not in the context, say you don't know.\n"
    prompt += "Always mention which part of the context you used.\n\n"
    prompt += "Context:\n" + context_text + "\n\n"
    prompt += "Question: " + question + "\n\nAnswer:"
    return prompt

def ask_ai(prompt):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": OPENROUTER_MODEL,
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    result = response.json()
    return result["choices"][0]["message"]["content"]

def answer_question(question):
    context_chunks = retrieve_context(question)
    prompt = build_prompt(question, context_chunks)
    return ask_ai(prompt)

if __name__ == "__main__":
    test_question = "ma heya aarad al kasr"
    print(answer_question(test_question))
