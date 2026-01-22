import os
import numpy as np
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from sklearn.metrics.pairwise import cosine_similarity

from chunk_fixed import run_fixed_strategy
from chunk_recursive import run_recursive_strategy
from chunk_semantic import run_semantic_strategy

load_dotenv()

def calculate_relevance_score(vectorstore, query, embeddings):
    """Calculates the mathematical similarity between the query and retrieved chunks."""
    # 1. Embed the question
    query_vector = embeddings.embed_query(query)
    
    # 2. Retrieve top 3 chunks
    docs = vectorstore.similarity_search(query, k=3)
    
    # 3. Embed the retrieved chunks to get their vectors
    doc_vectors = [embeddings.embed_query(d.page_content) for d in docs]
    
    # 4. Calculate average cosine similarity
    similarities = cosine_similarity([query_vector], doc_vectors)[0]
    return np.mean(similarities) * 100  # Return as a percentage

def run_evaluation():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    
    questions = [
        "How do machine learning algorithms and aerodynamic data help Formula One teams?",
        "Explain the technical regulations of Formula One hybrid power units.",
        "How is big data used to predict song popularity on Spotify?"
    ]

    print("--- Starting Mathematical Benchmark (Threshold Scoring) ---")

    strategies = {
        "Fixed-Size": run_fixed_strategy(),
        "Recursive": run_recursive_strategy(),
        "Semantic": run_semantic_strategy()
    }

    leaderboard = {"Fixed-Size": 0, "Recursive": 0, "Semantic": 0}

    for name, files_dict in strategies.items():
        print(f"\nCalculating Threshold Scores for {name}...")
        
        all_text_chunks = []
        for chunks in files_dict.values():
            all_text_chunks.extend(chunks)

        if not all_text_chunks:
            continue

        vectorstore = FAISS.from_texts(all_text_chunks, embeddings)
        
        scores = []
        for q in questions:
            score = calculate_relevance_score(vectorstore, q, embeddings)
            scores.append(score)
        
        avg_score = sum(scores) / len(scores)
        leaderboard[name] = avg_score

    print("\n" + "="*30)
    print("🏆 CHUNKING LEADERBOARD (Similarity Threshold)")
    print("="*30)
    for method, score in sorted(leaderboard.items(), key=lambda x: x[1], reverse=True):
        status = "✅ PASS" if score > 70 else "⚠️ LOW RELEVANCE"
        print(f"{method}: {score:.2f}% | {status}")
    print("="*30)

if __name__ == "__main__":
    run_evaluation()