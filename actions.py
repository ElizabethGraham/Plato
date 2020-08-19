import pygame

pygame.mixer.init()

ACTION_PICTURES = {
    # Dictionary holding all the emotions and their corresponding pictures.
    # Will be converted to Emotion : LED values when Plato is fully built
    'SAD': pygame.image.load(r'PIC_SAD.png'),
    'WINK': pygame.image.load(r'PIC_WINK.png')}
ACTION_SOUNDS = {
    # Dictionary holding all the emotions and their corresponding noises.
    'WINK': pygame.mixer.Sound('sound_woowoo.wav'),
    'SAD': pygame.mixer.Sound('sound_annoyed.wav')}


def action_wink():
    print("Action: WINK")
    return 'WINK'
