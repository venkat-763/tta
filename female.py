from gtts import gTTS
import os

# A list of text segments you want to convert
text_list = [
    "This is the first file.",
    "This is the second file.",
    "And here is the third file.",
    "Finally, the fourth file."
]

# Loop through the list using enumerate to get both the index and the text
# index starts at 0, so we add 1 to start naming from 1.mp3
for index, text in enumerate(text_list):
    # Create the speech object
    tts = gTTS(text=text, lang='en', slow=False)
    
    # Define the filename as a string: "1.mp3", "2.mp3", etc.
    filename = f"{index + 1}.mp3"
    
    # Save the file
    tts.save(filename)
    print(f"Saved: {filename}")

print("All files have been converted and saved.") 
