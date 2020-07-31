import pygame
import time

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

characterEmotions = [pygame.image.load(r'/home/pi/Documents/Plato/Plato-master/plato_pics/ROBOT_HAPPY.png'),
                     pygame.image.load(r'/home/pi/Documents/Plato/Plato-master/plato_pics/ROBOT_SAD.png'),
                     pygame.image.load(r'/home/pi/Documents/Plato/Plato-master/plato_pics/ROBOT_WINK.png')]

isHappy = True
isWinking = False
isSad = False

# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(white)


def emotion_happy():
    print("HAPPY")  # Print to console the function is runnning, for debug purposes
    emotion = 0  # Happy image in characterEmotions image array
    display_surface.blit(background, (0, 0))  # Reset canvas
    display_surface.blit(characterEmotions[emotion], (0, 0))  # Print the happy emotion picture
    # Play characterEmotionSound>Happy


def emotion_sad():
    print("SAD")
    emotion = 1
    display_surface.blit(background, (0, 0))
    display_surface.blit(characterEmotions[emotion], (0, 0))


def action_wink():
    print("WINK")
    emotion = 2
    display_surface.blit(background, (0, 0))
    display_surface.blit(characterEmotions[emotion], (0, 0))


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.update()

    emotion = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        emotion_happy()
    elif keys[pygame.K_RIGHT]:
        action_wink()
    elif keys[pygame.K_DOWN]:
        emotion_sad()

    # Flip the display
    pygame.time.delay(100)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()
