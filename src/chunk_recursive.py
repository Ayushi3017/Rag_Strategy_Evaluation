import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

def run_recursive_strategy():
    data_dir = "wiki_data"
    results = {}
    
    # Initialize the smarter splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )

    for i in range(1, 101):
        file_path = os.path.join(data_dir, f"{i}.txt")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # split_text returns a list of strings
                file_chunks = splitter.split_text(content)
                results[i] = file_chunks
                
    print(f"Recursive Chunking Complete: Processed {len(results)} files.")
    return results

if __name__ == "__main__":
    data = run_recursive_strategy()
    print(f"File 1 Chunks: {len(data[1])}")