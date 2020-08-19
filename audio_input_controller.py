import pyaudio
import numpy as np
import emotions
import plato_alpha


def init_listener():
    CHUNK = 2048
    RATE = 44100

    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    while True:  # Run the listener indefinitely
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        peak = np.average(np.abs(data)) * 2
        bars = "#" * int(50 * peak / 2 ** 16)
        print("%05d %s" % (peak, bars))  # Alternative: print("%04d %05d %s" % (peak, bars))
        level_monitor(peak)


def level_monitor(levels):  # Monitor audio levels: If levels exceed or equal 8000, change emotion to sad.
    if levels >= 8000:
        plato_alpha.update_emotion(emotions.emotion_sad())


# Main function
def main():
    init_listener()


if __name__ == "__main__":
    main()
