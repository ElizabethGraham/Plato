import pygame
import time
# import audio_input
# import motor_controller
# import text_to_speech

pygame.init()

# assigning values to X and Y variable 
X = 360
Y = 370

# define the RGB value 
# for white colour 
white = (255, 255, 255)

# Set up the drawing window
screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption("Plato Alpha")

# create the display surface object
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(white)


def change_picture():
    emotions = Emotions()

    CHARACTER_EMOTIONS = {'HAPPY': pygame.image.load(r'/plato_pics/ROBOT_HAPPY.png'),
                          'SAD': pygame.image.load(r'/plato_pics/ROBOT_SAD.png'),
                          'WINK': pygame.image.load(r'/plato_pics/ROBOT_WINK.png'),
                          'SURPRISED': pygame.image.load(r'/plato_pics/ROBOT_SURPRISED.png'),
                          'ALERT': pygame.image.load(r'/plato_pics/ROBOT_ALERT.png')}

    display_surface.blit(background, (0, 0))  # Reset canvas
    display_surface.blit(CHARACTER_EMOTIONS[emotions.emotion_state], (0, 0))  # Print the happy emotion picture


class Emotions:

    def __init__(self, state):
        self.emotion_state = state
        print("init")

    def emotion_happy(self):
        print("HAPPY")  # Print to console the function is running, for debug purposes
        self.emotion_state = 'HAPPY'
        return self.emotion_state  # Happy image in characterEmotions image array
        # Play characterEmotionSound>Happy in the future

    def emotion_sad(self):
        print("SAD")
        self.emotion_state = 'SAD'
        return

    def emotion_wink(self):
        print("WINK")
        self.emotion_state = 'WINK'
        return self.emotion_state

    def action_surprised(self):
        print("SURPRISED")
        self.emotion_state = 'SURPRISED'
        return self.emotion_state

    def action_alert(self):
        print("ALERT")
        self.emotion_state = 'ALERT'
        return self.emotion_state


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        Emotions.emotion_happy()
    elif keys[pygame.K_RIGHT]:
        Emotions.emotion_wink()
    elif keys[pygame.K_DOWN]:
        Emotions.emotion_sad()

    # Flip the display
    pygame.time.delay(100)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
