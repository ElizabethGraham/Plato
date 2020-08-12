import pygame

pygame.mixer.init()

EMOTION_PICTURES = {
    # Dictionary holding all the emotions and their corresponding pictures.
    # Will be converted to Emotion : LED values when Plato is fully built
    'HAPPY': pygame.image.load(r'PIC_HAPPY.png'),
    'SAD': pygame.image.load(r'PIC_SAD.png'),
    'WINK': pygame.image.load(r'PIC_WINK.png'),
    'SURPRISED': pygame.image.load(r'PIC_SURPRISED.png'),
    'ALERT': pygame.image.load(r'PIC_ALERT.png')}
EMOTION_SOUNDS = {
    # Dictionary holding all the emotions and their corresponding noises.
    'HAPPY': pygame.mixer.Sound('sound_woowoo.wav'),
    'SAD': pygame.mixer.Sound('sound_annoyed.wav'),
    'CONFUSED': pygame.mixer.Sound('sound_CONFUSED.wav'),
    'ANGRY': pygame.mixer.Sound('sound_angry.wav')}


def emotion_happy():
    print("HAPPY")  # Print to console the function is running, for debug purposes
    emotion_state = 'HAPPY'
    return emotion_state  # Return HAPPY as emotion state
    # Play characterEmotionSound>Happy in the future


def emotion_sad():
    print("SAD")
    emotion_state = 'SAD'
    return emotion_state


def emotion_wink():
    print("WINK")
    emotion_state = 'WINK'
    return emotion_state


def emotion_surprised():
    print("SURPRISED")
    emotion_state = 'SURPRISED'
    return emotion_state


def emotion_alert():
    print("ALERT")
    emotion_state = 'ALERT'
    return emotion_state


def update_emotion(state):
    # Update all emotion related objects. Change picture, play emotion sound, etc
    pass
    # Reset canvas
    # display_surface.blit(background, (0, 0))
    # Print the happy emotion picture
    # display_surface.blit(EMOTION_PICTURES[state], (0, 0))
