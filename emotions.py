import pygame

pygame.mixer.init()

class emotion_states(object):
    EMOTION_PICTURES = {
        # Dictionary holding all the emotions and their corresponding pictures.
        # Will be converted to Emotion : LED values when Plato is fully built
        'HAPPY': pygame.image.load(r'PIC_HAPPY.png'),
        'SAD': pygame.image.load(r'PIC_SAD.png'),
        'SURPRISED': pygame.image.load(r'PIC_SURPRISED.png'),
        'ALERT': pygame.image.load(r'PIC_ALERT.png')}
    EMOTION_SOUNDS = {
        # Dictionary holding all the emotions and their corresponding noises.
        'HAPPY': pygame.mixer.Sound('sound_woowoo.wav'),
        'SAD': pygame.mixer.Sound('sound_annoyed.wav'),
        'CONFUSED': pygame.mixer.Sound('sound_CONFUSED.wav'),
        'ANGRY': pygame.mixer.Sound('sound_angry.wav')}

    emotion_state = ""

    def emotion_happy(self):
        print("HAPPY")  # Print to console the function is running, for debug purposes
        emotion_state = 'HAPPY'
        return emotion_state  # Return HAPPY as emotion state
        # Play characterEmotionSound>Happy in the future

    def emotion_sad(self):
        print("SAD")
        emotion_state = 'SAD'
        return emotion_state

    def emotion_surprised(self):
        print("SURPRISED")
        emotion_state = 'SURPRISED'
        return emotion_state

    def emotion_alert(self):
        print("ALERT")
        emotion_state = 'ALERT'
        return emotion_state


def determine_emotion():
# Emotions should be determined on a logarithmic scale; where the more significant the stimulus, the better the
# odds of the emotion being changed.
