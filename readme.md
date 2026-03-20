# 🚀 RAG System (From Scratch - Windows + VS Code)

This project demonstrates how to build a **Retrieval-Augmented Generation (RAG)** system from scratch using OpenAI, LangChain, and ChromaDB.

---

## 📌 What We’re Building

A **RAG system** that:

* Turns documents into searchable vectors
* Finds information using semantic search
* Sends relevant context to the LLM
* Generates accurate answers from your data

---

## 🛠️ Setup Guide (Windows + VS Code)

### 🔑 Step 1: OpenAI API Key Setup

1. Go to OpenAI Platform:
   https://platform.openai.com/chat

2. Complete billing/project setup (if prompted)

3. Open API Keys page:
   https://platform.openai.com/api-keys

4. Click **"Create new secret key"**

   * Name: `rag-local-dev`
   * Permissions: `All` (or Restricted for safer setup)

5. Copy the key immediately (cannot be viewed again)

---

### 💳 Billing & Limits

* Billing Overview:
  https://platform.openai.com/settings/organization/billing/overview

* Usage Limits:
  https://platform.openai.com/settings/organization/limits

---

## ⚙️ Environment Setup (VS Code Terminal - PowerShell)

```powershell
cd "C:\Users\Annamalai\Desktop\rag-system"

python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### If activation fails:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

---

### 📦 Install Dependencies

```powershell
python -m pip install --upgrade pip
pip install openai chromadb langchain langchain-community tiktoken pypdf python-dotenv
```

---

### 🔐 Set OpenAI API Key

```powershell
$env:OPENAI_API_KEY="sk-YOUR_KEY"
setx OPENAI_API_KEY "sk-YOUR_KEY"
```

Restart VS Code terminal and verify:

```powershell
python -c "import os; print('FOUND' if os.getenv('OPENAI_API_KEY') else 'MISSING')"
```

---

## 📁 Project Structure

```powershell
cd "C:\Users\Annamalai\Desktop\rag-system"

mkdir data\raw -Force
mkdir data\chroma -Force
mkdir src -Force
```

Place your test PDF here:

```
C:\Users\Annamalai\Desktop\rag-system\data\raw\docs.pdf
```

---

## ✅ Verification Steps

### 🔍 Check API Key

```powershell
python -c "import os; print('OPENAI_API_KEY OK' if os.getenv('OPENAI_API_KEY') else 'OPENAI_API_KEY MISSING')"
```

### 🤖 Test OpenAI API

```powershell
python -c "from openai import OpenAI; c=OpenAI(); r=c.responses.create(model='gpt-4o-mini', input='Reply with: API working'); print(r.output_text)"
```

---

## 🔄 Run RAG Pipeline

### 📥 Step 1: Ingest Data (Build Vector DB)

```powershell
python src/main.py ingest --pdf data/raw/docs.pdf
```

### ❓ Step 2: Ask Questions

```powershell
python src/main.py ask --q "What is this document about?"
```

```powershell
python src/main.py ask --q "List 3 key points from the document."
```

---

## 🧠 RAG Pipeline Overview

1. Load PDF documents
2. Split into chunks
3. Generate embeddings
4. Store in ChromaDB
5. Retrieve relevant chunks
6. Select top results (best context)
7. Build prompt with context
8. Generate answer using LLM

---

## ⚠️ Common Issue: 429 (insufficient_quota)

This is **NOT a code issue** — it's a billing/quota problem.

### ✅ Fix Steps

1. Enable billing:

   * https://platform.openai.com/settings/organization/billing/overview

2. Increase usage limits:

   * https://platform.openai.com/settings/organization/limits

3. Generate new API key:

```powershell
setx OPENAI_API_KEY "sk-NEW_KEY"
```

4. Restart terminal

5. Re-run test:

```powershell
python test_openai.py
```

---

## 💡 Important Notes

* OpenAI API is **paid based on usage**

* Costs depend on:

  * Tokens used
  * Model selected

* The error `insufficient_quota` usually means:

  * No active billing
  * Free credits exhausted
  * Usage limits reached

* Control spending via:

  * Soft limits (alerts)
  * Hard limits (cutoff)

---

## 🚀 Production Improvements

To enhance your RAG system:

* Add **reranking** for better search results
* Use **metadata filtering** to refine retrieval
* Log retrieved chunks for debugging
* Evaluate performance using **RAGAS**

---

## 🎯 Summary

You now have a fully working:

✅ Local RAG system
✅ Vector database (ChromaDB)
✅ Semantic search pipeline
✅ LLM-powered Q&A over your documents

---

Happy Building! 🚀
