from gtts import gTTS
from pygame import mixer

file_name = "sound_howBig.mp3"
tts = gTTS(text='How big I am?', lang='en')
try:
    tts.save("sound_howBig.mp3")
except:
    pass

mixer.init()
mixer.music.load('sound_howBig.mp3')
mixer.music.play()
