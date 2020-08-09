import pygame


class Emotions:
    EMOTION_PICTURES = {
        # Dictionary holding all the emotions and their corresponding pictures.
        # Will be converted to Emotion : LED values when Plato is fully built
        'HAPPY': pygame.image.load(r'ROBOT_HAPPY.png'),
        'SAD': pygame.image.load(r'C:\Users\jtgra\PycharmProjects\Plato/plato_pics/ROBOT_SAD.png'),
        'WINK': pygame.image.load(r'C:\Users\jtgra\PycharmProjects\Plato/plato_pics/ROBOT_WINK.png'),
        'SURPRISED': pygame.image.load(r'C:\Users\jtgra\PycharmProjects\Plato/plato_pics/ROBOT_SURPRISED.png'),
        'ALERT': pygame.image.load(r'C:\Users\jtgra\PycharmProjects\Plato/plato_pics/ROBOT_ALERT.png')}
    EMOTION_SOUNDS = {
        # Dictionary holding all the emotions and their corresponding noises.
        'HAPPY': pygame.mixer.Sound(''),
        'SAD': pygame.mixer.Sound(''),
        'WINK': pygame.mixer.Sound(''),
        'SURPRISED': pygame.mixer.Sound(''),
        'ALERT': pygame.mixer.Sound('')}

    def __init__(self, state):
        # All functions should return an emotion state
        self.emotion_state = state
        print("init")

    def emotion_happy(self):
        print("HAPPY")  # Print to console the function is running, for debug purposes
        self.emotion_state = 'HAPPY'
        return self.emotion_state  # Return HAPPY as emotion state
        # Play characterEmotionSound>Happy in the future

    def emotion_sad(self):
        print("SAD")
        self.emotion_state = 'SAD'
        return self.emotion_state

    def emotion_wink(self):
        print("WINK")
        self.emotion_state = 'WINK'
        return self.emotion_state

    def emotion_surprised(self):
        print("SURPRISED")
        self.emotion_state = 'SURPRISED'
        return self.emotion_state

    def emotion_alert(self):
        print("ALERT")
        self.emotion_state = 'ALERT'
        return self.emotion_state
