import pyaudio
import numpy as np
import emotions


def init_listener():
    CHUNK = 2048
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    while True:  # Run the listener indefinitely
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        peak = np.average(np.abs(data)) * 2
        bars = "#" * int(50 * peak / 2 ** 16)
        print("%05d %s" % (peak, bars))  # Alternative: print("%04d %05d %s" % (peak, bars))
        level_monitor(peak)


def level_monitor(levels):
    if levels >= 8000:
        return emotions.emotion_sad()
