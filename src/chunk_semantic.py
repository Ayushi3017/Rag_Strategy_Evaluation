import os
import time
from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# 1. Force reload of .env to ensure it sees the latest changes
load_dotenv()

def run_semantic_strategy():
    # 2. Extract the key clearly
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ Error: GOOGLE_API_KEY not found in .env file.")
        return {}

    # 3. Initialize embeddings with the specific model you chose
    print("Initializing Google Embeddings for Semantic Chunking...")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=api_key
    )
    
    # 4. Initialize the semantic splitter
    splitter = SemanticChunker(embeddings)
    
    data_dir = "wiki_data"
    results = {}

    print("Starting Semantic Chunking (this takes longer than the others)...")

    # 5. Loop through your 100 files
    for i in range(1, 101):
        file_path = os.path.join(data_dir, f"{i}.txt")
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    
                    # AI-powered splitting happens here
                    file_chunks = splitter.split_text(content)
                    results[i] = file_chunks
                    
                    print(f"✅ Chunked {i}/100: (Found {len(file_chunks)} chunks)")
                    
                    # 6. Politeness delay to avoid "Resource Exhausted" 429 errors
                    time.sleep(1) 
                    
            except Exception as e:
                print(f"⚠️ Error processing file {i}: {e}")
                continue

    print("\n--- Semantic Chunking Strategy Complete ---")
    return results

if __name__ == "__main__":
    # Test run
    data = run_semantic_strategy()
    if data:
        print(f"Total files processed: {len(data)}")