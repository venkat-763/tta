import pyttsx3
import time

text_list = [
    "First audio file generated.",
    "Second audio file generated.",
    "Third audio file generated.",
    "Fourth audio file generated.",
    "Fifth audio file generated."
]

for index, text in enumerate(text_list):
    filename = f"{index + 1}.mp3"
    print(f"Starting conversion for: {filename}")
    
    engine = pyttsx3.init()
    
    engine.setProperty('rate', 150)
    
    engine.save_to_file(text, filename)
    
    engine.runAndWait()
    
    engine.stop()
    del engine 
    
    time.sleep(1) 
    print(f"Successfully saved: {filename}")

print("Done! Check your folder for all files.")
