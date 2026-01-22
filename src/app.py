import wikipedia
import os
import time

# 1. Setup
SAVE_DIR = "wiki_data"
os.makedirs(SAVE_DIR, exist_ok=True)

# 2. Your specific interests (Seeds)
seed_topics = ["Natural Language Processing", "Machine Learning", "Formula One", "Data Analysis", "Artificial Intelligence","Shah Rukh Khan","The Office","Brooklyn 99","Stockholm"]

def download_specific_topics(target_count=100):
    downloaded = 0
    
    for seed in seed_topics:
        if downloaded >= target_count:
            break
            
        print(f"Searching for articles related to: {seed}")
        # search() returns a list of related article titles
        related_titles = wikipedia.search(seed, results=25) 
        
        for title in related_titles:
            if downloaded >= target_count:
                break
                
            try:
                page = wikipedia.page(title, auto_suggest=False)
                
                # Use a number for the filename as requested
                file_number = downloaded + 1
                filename = os.path.join(SAVE_DIR, f"{file_number}.txt")
                
                with open(filename, "w", encoding="utf-8") as f:
                    # We save the title on the first line so we don't forget what's in it
                    f.write(f"TITLE: {title}\n\n")
                    f.write(page.content)
                
                downloaded += 1
                print(f"Saved [{downloaded}/{target_count}]: {title}")
                
            except (wikipedia.DisambiguationError, wikipedia.PageError, Exception):
                # Skip errors and keep moving
                continue

    print(f"\nFinished! {downloaded} files are in the '{SAVE_DIR}' folder.")

if __name__ == "__main__":
    download_specific_topics(100)