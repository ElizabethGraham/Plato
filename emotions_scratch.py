import pygame

pygame.mixer.init()


class Emotions(object):
    def __init__(self, emotion_state, action_state):
        """Constructor"""
        self.life_state = life_state
        self.emotion_state = emotion_state
        self.action_state = action_state

    EMOTION_STATE = {
        'HAPPY': (pygame.image.load(r'PIC_HAPPY.png'), pygame.mixer.Sound('sound_woowoo.wav')),
        'SAD': (pygame.image.load(r'PIC_SAD.png'), pygame.mixer.Sound('sound_annoyed.wav')),
        'SURPRISED': (pygame.image.load(r'PIC_SURPRISED.png'), ),
        'ANGRY': (pygame.image.load(r'PIC_ANGRY.png'), pygame.mixer.Sound('sound_angry.wav'))}

    def update_emotion(self, pygame_surface, background, emotion_state):
        # Update all emotion related objects. Change picture, play emotion sound, etc
        # Reset canvas
        pygame_surface.blit(background, (0, 0))

        # Print the happy emotion picture
        pygame_surface.blit(EMOTION_PICTURES[emotion_state], (0, 0))

        # Try to play emotion's corresponding sound file, in case emotion does not have assigned sound
        try:
            pygame.mixer.Sound.play(emotions.EMOTION_SOUNDS[emotion_state])
        except AttributeError:
            print("Sound N/A")