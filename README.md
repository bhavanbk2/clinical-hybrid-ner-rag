# 🧠 Clinical Hybrid NER-RAG-LLM Framework

A universal NLP framework designed to extract and interpret clinical data from both structured **tabular records** and unstructured **doctor’s notes** using **Named Entity Recognition (NER)**, **contextual serialization**, and **Retrieval-Augmented Generation (RAG)** powered by **Large Language Models (LLMs)** like GPT-4o.

---

## 📌 Objective

To develop a domain-adapted, LLM-enhanced system that:
- Extracts clinical entities from structured **tabular datasets**.
- Converts tabular data into **context-rich narratives**.
- Combines these narratives with unstructured text in a **hybrid RAG setup**.
- Uses LLMs to provide **diagnostic insights and medical information**.
- Benchmarks against **GPT-4o** to validate performance improvements.

---

## 🔍 Key Features

- 🔬 **Clinical NER** using domain-specific models (e.g., BioClinicalBERT).
- 🧾 **Tabular-to-Text Serialization**: Automatically generate readable narratives from structured tables.
- 🔁 **Hybrid RAG**: Retrieve relevant data from both tabular and text sources for LLM input.
- 🧠 **LLM-Powered Diagnosis**: Use fine-tuned or API-based LLMs (like GPT-4o) for medical reasoning.
- ✅ **Evaluation-ready**: Compare model output using Precision, Recall, F1, BLEU, and clinical expert feedback.

---

## 📁 Project Structure

clinical-hybrid-ner-rag-llm/ 
    ├── data/ 
        # Clinical notes and tabular datasets 
    ├── src/ 
        # Main logic: NER, serialization, RAG, LLM 
        │ ├── ner.py │ 
        ├── serializer.py │ 
        ├── rag.py │ 
        ├── llm_inference.py 
        │ └── utils.py 
    ├── notebooks/ 
        # Experimentation and benchmarking 
        │ └── experiments.ipynb 
    ├── requirements.txt 
    ├── README.md 
    └── .gitignore
---

## ⚙️ Installation

```bash
git clone https://github.com/bhavanbk2/clinical-hybrid-ner-rag-llm.git
cd clinical-hybrid-ner-rag-llm
python -m venv env
source env/bin/activate
pip install -r requirements.txt
