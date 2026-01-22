import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_embeddings(chunks):
    """
    Takes a list of text strings and returns their vector embeddings 
    using the Gemini models/text-embedding-004 model.
    """
    if not chunks:
        return []
    
    # Using the latest Gemini embedding model
    model = "models/text-embedding-004"
    
    try:
        result = genai.embed_content(
            model=model,
            content=chunks,
            task_type="retrieval_document"
        )
        return result['embedding']
    except Exception as e:
        print(f"Error generating embeddings: {e}")
        return []

if __name__ == "__main__":
    # Test with a sample chunk
    sample = ["Formula One engines use MGU-H and MGU-K systems."]
    vector = get_embeddings(sample)
    print(f"Successfully generated vector of length: {len(vector[0])}")