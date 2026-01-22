# RAG Chunking Strategy: The Great Bake-Off 🥨

**An empirical evaluation of text-splitting strategies for high-accuracy retrieval-augmented generation.**

## 📊 Performance Leaderboard

| Strategy | Similarity Score | Status | Key Strength |
| --- | --- | --- | --- |
| **Recursive** | **63.84%** | 🏆 **Champion** | Best alignment with Wikipedia's structural logic |
| **Fixed-Size** | **61.33%** | 🥈 **Runner Up** | Consistent chunk density for vector search |
| **Semantic** | **60.82%** | 🥉 **Third Place** | High thematic sensitivity |

---

## 🚀 Overview

This project benchmarks three distinct text-chunking methodologies to solve the "Context Window" problem in RAG systems. Using a dataset of **100 Wikipedia articles** (covering Formula One, Machine Learning, and Spotify data), we evaluated how each strategy influences the mathematical relevance of retrieved context.

### The Problem

Large documents must be split into smaller "chunks" to fit within LLM context windows. However, splitting data blindly often leads to "broken logic" where a chunk loses the very information needed to answer a query.

---

## 🛠️ Technical Stack

* **Language:** Python
* **Orchestration:** LangChain
* **Vector Database:** FAISS
* **Embeddings:** Google Gemini (`text-embedding-004`)

---

## 🔍 Strategies Evaluated

### 1. Recursive Character Chunking (The Winner)

* **Logic:** Uses a hierarchy of separators (`\n\n`, `\n`, ` `) to split text while respecting paragraph and sentence boundaries.
* **Result:** Achieved the highest score by preserving the structural integrity of Wikipedia's paragraph-based layout.

### 2. Fixed-Size Chunking

* **Logic:** Splits text at a hard character count (1000 chars) with a 100-character overlap.
* **Result:** Performed surprisingly well due to consistent vector density, but occasionally fragmented technical context.

### 3. Semantic Chunking

* **Logic:** Uses AI embeddings to detect "topic shifts" within the text, only splitting when the meaning changes.
* **Result:** Third place. Likely over-segmented Wikipedia's technical prose, proving that "AI-driven" splitting isn't always superior to structural splitting.

---

## 🧪 Methodology

1. **Ingestion:** 100 articles were scraped and cleaned from Wikipedia.
2. **Vectorization:** Chunks were converted into 768-dimensional vectors.
3. **Scoring:** We utilized a **Mathematical Threshold Score** based on Average Cosine Similarity.
4. **Verification:** A multi-question benchmark was run to ensure result consistency across different domains (F1 vs. AI).

---

## 📂 Project Structure

* `app.py` - Wikipedia data downloader.
* `chunk_fixed.py` - Fixed-size splitting logic.
* `chunk_recursive.py` - Structural splitting logic.
* `chunk_semantic.py` - Embedding-based splitting logic.
* `Score.py` - Mathematical evaluation & leaderboard generation.
* `.env` - API configuration.

---

## 🏆 Key Findings

* **Structure Matters:** **Recursive Chunking** is the optimal choice for well-organized data like Wikipedia, as it respects natural paragraph breaks.
* **The Hype Gap:** Semantic chunking is powerful but can be overly sensitive to minor topic shifts, leading to fragmented context in technical documentation.
* **Robust Embeddings:** The narrow margin between strategies (~3%) indicates that the `text-embedding-004` model is highly resilient at finding relevance regardless of the split method.
