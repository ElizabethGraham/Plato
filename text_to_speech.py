from gtts import gTTS
from pygame import mixer

file_name = "how-big.mp3"
tts = gTTS(text='How big I am?', lang='en')
try:
    tts.save("how-big.mp3")
except:
    pass

mixer.init()
mixer.music.load('how-big.mp3')
mixer.music.play()
