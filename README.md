# Tvara AI Challenge

This repository contains my solutions for the Tvara AI technical challenge.

---

## Task B – Gemini CLI

### Description
A simple Python CLI that accepts a prompt and forwards it to the Google Gemini
`generateContent` API, printing the model response to the terminal.

### How to Run
export GEMINI_API_KEY="YOUR_API_KEY"

python task_b_gemini_cli.py "Explain RAG in 2 lines"

### Note on API Key
The provided Gemini API key returns a 403 / 429 error due to being flagged as
leaked or having zero available quota on Google's side.  
This is a key-level / quota-level limitation, not an implementation issue.

---

## Task C – Vectorization with Hugging Face

### Description
Uses the intfloat/e5-small-v2 sentence-transformer model to generate embeddings
for a small set of sentences and perform cosine similarity search to retrieve
the most relevant sentence for a given query.

### How to Run
python task_c_embeddings.py

---


