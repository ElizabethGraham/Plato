import pygame
import time
import emotions
# import audio_input
# import motor_controller
# import text_to_speech

pygame.init()
emotions_script = emotions.Emotions('HAPPY')

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


def change_picture(state):
    # Reset canvas
    display_surface.blit(background, (0, 0))
    # Print the happy emotion picture
    # display_surface.blit(emotions_script.CHARACTER_EMOTIONS[emotions_script.emotion_state], (0, 0))
    display_surface.blit(emotions_script.CHARACTER_EMOTIONS[state], (0, 0))


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.update()

    keys = pygame.key.get_pressed()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:

            if keys[pygame.K_SPACE]:
                emotions_script.emotion_happy()
                change_picture()
            elif keys[pygame.K_RIGHT]:
                emotions_script.emotion_wink()
            elif keys[pygame.K_DOWN]:
                emotions_script.emotion_sad()

    # Flip the display
    pygame.time.delay(100)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
