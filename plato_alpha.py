import pygame
import time
import emotions
import audio_input_controller
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


def change_picture(state):
    # Reset canvas
    display_surface.blit(background, (0, 0))
    # Print the happy emotion picture
    display_surface.blit(emotions.EMOTION_PICTURES[state], (0, 0))


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.update()

    keys = pygame.key.get_pressed()
    # If an emotion key is pressed, change Plato's picture to represent the new emotion
    if keys:
        if keys[pygame.K_SPACE]:
            change_picture(emotions.emotion_happy())
        elif keys[pygame.K_RIGHT]:
            change_picture(emotions.emotion_wink())
        elif keys[pygame.K_DOWN]:
            change_picture(emotions.emotion_sad())

    # If audio input exceeds 8000 peak, change Plato's emotion to scared
    # if audio_input_controller.init_listener.:

    # Flip the display
    pygame.time.delay(100)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
