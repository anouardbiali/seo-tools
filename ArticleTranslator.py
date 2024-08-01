from deep_translator import GoogleTranslator
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random
#from pathlib import Path
import os



def translate(text, source, target):
    translator = GoogleTranslator() # YOU MUST CREATE ONE FOR EACH REQUEST OR THE MULTI-THREADING WILL FAIL, SINCE EACH INSTANCE HANDLE ONE REQUEST AT a TIME.
    translator.source = source
    translator.target = target
    return translator.translate(text)

def translate_and_save(source_path, save_path, source_lang, target_lang, max_chunk_length, num_workers):
    try:
        if not source_lang or not target_lang:
            raise ValueError("Please select both source and target languages")

        # Split the text lines into chunks of 5000 chars each
        chunks = []
        current_chunk = ""
        with open(source_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if len(current_chunk) + len(line) < max_chunk_length:
                    current_chunk += line
                else:
                    chunks.append(current_chunk)
                    current_chunk = line

            # Append the remaining chunk if any
            if current_chunk:
                chunks.append(current_chunk)
        n_chunks = len(chunks)

        # Multi-Threading
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [
                executor.submit(
                    lambda text: translate(text, source_lang, target_lang),
                    chunk
                ) for chunk in chunks
            ]

            for i, future in enumerate(as_completed(futures)):
                # Update progress bar
                print((i + 1) * 100 // n_chunks)


        # Saving
        translated_text = "\n".join([future.result() for future in futures])
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(translated_text)
            

        print("translation completed")

    except Exception as e:
        print(e)

def start_translation(source_path,save_path,source_lang,target_lang):

    #Need to be in the worker : ===== 
    # source_path = input("Path to input folder: ")
    # save_path = input("Path to output folder: ")
    # source_lang = input("Source language code (e.g. 'en'): ")
    # target_lang = input("Target language code (e.g. 'fr'): ")
    max_chunk_length = 5000

    # Create output folder if it doesn't exist
    #Path(save_path).mkdir(parents=True, exist_ok=True)
    
    # Iterate through files in the input folder
    for filename in os.listdir(source_path):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(source_path, filename)  # Full path to input file
            output_file_path = os.path.join(save_path, f"translated_{filename}")  # Full path to output file
            num_workers = 4
            translate_and_save(input_file_path, output_file_path, source_lang, target_lang, max_chunk_length, num_workers)
            print(f"{filename} is translated successfully")
            tmemail = random.randint(10,15)
            time.sleep(tmemail)
            
    

def start_translation_thread():
    new_thread = threading.Thread(target=start_translation)
    new_thread.start()
    new_thread.join() 






