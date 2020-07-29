from gtts import gTTS
import os

# The text that you want to convert to audio
mytext = 'How big I am?'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("how-big-i-am.mp3")

# Playing the converted file
os.system("mpg321 how-big-i-am.mp3")
print("How big I am?")