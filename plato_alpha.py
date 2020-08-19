import pygame
import time
import actions
import emotions

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


def update_emotion(emotion_state):
    # Update all emotion related objects. Change picture, play emotion sound, etc
    # Reset canvas
    display_surface.blit(background, (0, 0))

    # Print the happy emotion picture
    display_surface.blit(emotions.EMOTION_PICTURES[emotion_state], (0, 0))

    # Try to play emotion's corresponding sound file, in case emotion does not have assigned sound
    try:
        pygame.mixer.Sound.play(emotions.EMOTION_SOUNDS[emotion_state])
    except AttributeError:
        print("Sound N/A")


def update_action(action):
    update_action.has_been_called = True
    # Call action
    # Return Plato to previous state
    # Reset canvas
    display_surface.blit(background, (0, 0))

    # Display the action picture
    display_surface.blit(actions.ACTION_PICTURES[action], (0, 0))


update_action.has_been_called = False

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.update()

    # If an action has been updated, delay for 1 second, then reset Plato to happy
    if update_action.has_been_called:
        # Default emotion state
        pygame.time.delay(1000)
        update_emotion(emotions.emotion_happy())
        update_action.has_been_called = False

    keys = pygame.key.get_pressed()
    # If an emotion key is pressed, change Plato's picture to represent the new emotion
    # Can change to keypress_dict, this is a work in progress to see flow of thought
    if keys:
        if keys[pygame.K_SPACE]:
            update_emotion(emotions.emotion_happy())
        elif keys[pygame.K_RIGHT]:
            update_action(actions.action_wink())
            # time.sleep(1)
            # update_emotion(emotions.emotion_happy())
        elif keys[pygame.K_DOWN]:
            update_emotion(emotions.emotion_sad())

    # If audio input exceeds 8000 peak, change Plato's emotion to scared
    # Flip the display
    pygame.time.delay(100)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
