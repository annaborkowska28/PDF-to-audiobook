
from gtts import gTTS
from pypdf import PdfReader
# import os to play the converted audio
import os


#this will read pdf file
reader = PdfReader('my_text.pdf') #add your own file pdf
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

language = 'en'


my_converted_song = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named "music.mp3"
my_converted_song.save("music.mp3")

# Playing the converted file
os.system("start music.mp3")