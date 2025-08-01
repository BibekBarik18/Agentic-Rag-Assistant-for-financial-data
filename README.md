# Agentic RAG Assistant for Financial Data

An **Agentic Retrieval-Augmented Generation (RAG) Assistant** designed for financial data analysis, powered by **LangGraph**, **Groq LLMs**, and **MCP (Model Context Protocol)** servers. This project combines the intelligence of large language models with custom-built financial tools to provide accurate, context-driven insights for finance-related queries.

---

## 🚀 Features

* **📂 Document Ingestion**

  * Upload CSV financial datasets directly from the UI
  * Chunking and embedding with **Ollama Embeddings**
  * Indexed and stored in **FAISS vector database**

* **🔍 Smart Retrieval**

  * Semantic search for highly relevant context
  * Ensures responses are grounded in your uploaded data

* **🤖 Agentic Workflow**

  * Built with **LangGraph** for modular agent design
  * Agents for ingestion, retrieval, and LLM-based responses
  * Tool invocation only when required

* **⚙️ MCP Tool Server Integration**

  * Custom **financial tools** via **FastMCP** including:

    * Debt-to-Equity Ratio
    * ROI (Return on Investment)
    * Net Profit Margin
    * Revenue Growth
    * Basic Arithmetic Operations (Add, Subtract, Multiply, Divide)
  * Tools accessible from both:

    * **Claude Desktop via MCP protocol**
    * **Custom Streamlit-based web application**

* **⚡ Fast & Efficient Responses**

  * LLM responses powered by **Groq’s Llama-3.3-70B**
  * Optimized for speed and accuracy

---

## 📊 Workflow Overview

1. **Upload a CSV file** with financial data
2. **Ingestion Agent**: Splits and embeds data into FAISS
3. **Retrieval Agent**: Finds relevant chunks for your query
4. **LLM Response Agent**:

   * Generates answers using Groq LLM
   * Invokes MCP tools when calculations are needed
5. **Response Delivered** in the Streamlit UI or Claude Desktop

---

## 🛠️ Tech Stack

* **LangGraph** – Agentic RAG pipeline orchestration
* **LangChain** – Document loading & text splitting
* **Groq LLM (Llama-3.3-70B)** – High-speed reasoning
* **Ollama Embeddings** – Vector representation
* **FAISS** – Semantic vector search
* **MCP (Model Context Protocol)** – Tool integration
* **FastMCP** – MCP tool server
* **Streamlit** – User-friendly web interface

---

## ⚡ Getting Started

### Prerequisites

* Python 3.10+
* Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the MCP Tool Server

```bash
python tools_server.py
```

### Launch the Streamlit App

```bash
streamlit run web.py
```

### Usage

* Upload your **financial CSV file**
* Ask your financial query in the chat input
* View responses with **context + tool-assisted calculations**

---

## 🌐 MCP Integration

This project supports MCP tool execution:

* Directly via **Claude Desktop** for interactive agent workflows
* Through the **Streamlit web app** for a full-stack RAG experience

---

## 📌 Example Queries

* *“What is the debt-to-equity ratio of Company A?”*
* *“Compare the revenue growth from Q1 to Q2.”*
* *“What is the ROI of this investment?”*
* *“Add the total revenue of all companies.”*

---

## 🤝 Connect with Me

If you find this project interesting, let’s connect on [LinkedIn](https://www.linkedin.com/in/bibek-barik/)

\#AI #LangGraph #RAG #MCP #ClaudeAI #Streamlit #FinancialData #MachineLearning

---
