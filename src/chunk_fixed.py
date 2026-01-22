import os
from dotenv import load_dotenv

load_dotenv()

def fixed_size_chunking(text, chunk_size=1000, overlap=100):
    """Splits text into chunks of fixed character length."""
    chunks = []
    # We move through the text by (chunk_size - overlap) to maintain context
    for i in range(0, len(text), chunk_size - overlap):
        chunk = text[i : i + chunk_size]
        chunks.append(chunk)
    return chunks

def run_fixed_strategy():
    data_dir = "wiki_data"
    results = {}

    # Processing our 100 files
    for i in range(1, 101):
        file_path = os.path.join(data_dir, f"{i}.txt")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Create chunks
                file_chunks = fixed_size_chunking(content)
                results[i] = file_chunks
                
    print(f"Fixed Chunking Complete: Processed {len(results)} files.")
    return results

if __name__ == "__main__":
    data = run_fixed_strategy()
    # Check a sample from the first file
    print(f"File 1 has {len(data[1])} chunks.")
    print(f"First chunk sample: {data[1][0][:100]}...")