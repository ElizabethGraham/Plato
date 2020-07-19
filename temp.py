# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Plato Alpha")


# create a surface object, image is drawn on it. 
#happy = pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_HAPPY.png') 
#sad = pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_SAD.png') 
#wink = pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_WINK.png') 

characterEmotions = [pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_HAPPY.png'), pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_SAD.png'), pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_WINK.png')]

isHappy = True
isWinking = False
isSad = False

# define the RGB value 
# for white colour 
white = (255, 255, 255) 

clock = pygame.time.Clock()
  
# assigning values to X and Y variable 
X = 400
Y = 400

# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 

def characterHappy():
    while True:
        time.sleep(3)
        display_surface.blit(characterEmotions[0], (0,0))
def characterWink():
    while True:
        time.sleep(3)
        display_surface.blit(characterEmotions[1], (0,0))
def characterSad():
    while True:
        time.sleep(3)
        display_surface.blit(characterEmotions[2], (0,0))

def redrawGameWindow():
    # Fill the background with white
    screen.fill(white)
    
    if isHappy:
        characterHappy()
    elif isWinking:
        characterWink()
    elif isSad:
        characterSad()
        
    pygame.display.update() 
    

# Run until the user asks to quit
running = True
while running:
    clock.tick(27)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()  
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        print("space")
        isWinking = True
        redrawGameWindow()
    
    # Flip the display
    pygame.display.flip()
    
    redrawGameWindow() 
    
    

        
# Done! Time to quit.
pygame.quit()