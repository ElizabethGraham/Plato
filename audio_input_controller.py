import pyaudio
import numpy as np


# import plato_alpha

def init_audio_input_monitor():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    for i in range(int(10 * 44100 / 1024)):  # go for a few seconds
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        peak = np.average(np.abs(data)) * 2
        bars = "#" * int(50 * peak / 2 ** 16)
        # print("%04d %05d %s" % (i, peak, bars))
        print(peak)

        # if peak >= 8000:
        # Change emotion to scared
        # plato_alpha.

    stream.stop_stream()
    stream.close()
    p.terminate()


class Audio_Input:
    CHUNK = 2048
    RATE = 44100

    p = pyaudio.PyAudio()
