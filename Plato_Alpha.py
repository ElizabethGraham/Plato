# Simple pygame program

# Import and initialize the pygame library
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

characterEmotions = [pygame.image.load(r'/home/pi/Documents/Plato/Plato-master/plato_pics/ROBOT_HAPPY.png'), pygame.image.load(r'/home/pi/Documents/Plato/Plato-master/plato_pics/ROBOT_SAD.png'), pygame.image.load(r'/home/pi/Documents/Plato/Plato-master/plato_pics/ROBOT_WINK.png')]

isHappy = True
isWinking = False
isSad = False

# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(white)

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
        print("HAPPY")
        emotion = 0
        display_surface.blit(background, (0,0))
        display_surface.blit(characterEmotions[emotion], (0, 0))
    elif keys[pygame.K_RIGHT]:
        print("WINK")
        emotion = 2
        display_surface.blit(background, (0,0))
        display_surface.blit(characterEmotions[emotion], (0, 0))
    elif keys[pygame.K_DOWN]:
        print("SAD")
        emotion = 1
        display_surface.blit(background, (0,0))
        display_surface.blit(characterEmotions[emotion], (0, 0))
    
    # Flip the display
    pygame.time.delay(100)
    pygame.display.update()
     
# Done! Time to quit.
pygame.quit()