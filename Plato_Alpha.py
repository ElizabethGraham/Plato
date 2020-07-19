# Simple pygame program

# Import and initialize the pygame library
import pygame
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

characterEmotions = [pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_HAPPY.png'), pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_SAD.png'), pygame.image.load(r'C:\Users\jtgra\Pictures\Plato\ROBOT_WINK.png')]

isHappy = True
isWinking = False
isSad = False

# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()  
    
    display_surface.blit(characterEmotions[1], (0,0))
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE]:
        print("space")
        isWinking = True
    
    # Flip the display
    pygame.display.flip()
     
# Done! Time to quit.
pygame.quit()