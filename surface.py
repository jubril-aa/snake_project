import pygame, sys

pygame.init() # starts the pygame module 
cell_size = 30
cell_number = 20
screen  = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) # this sets the widow for the game and which size it will have
clock = pygame.time.Clock() # this is used so the while loops doesn't repeat itslef more then a certain time per second
test_surface = pygame.Surface((100, 200)) 

while True: 
    for event in pygame.event.get(): # this is the triger to stop the loop
        if event.type == pygame.QUIT: 
            pygame.quit() # stops all the pygame functions
            sys.exit() # because not all pygame functions are stoped above, this stops the rest 
        screen.fill((0,60,0)) # color of the screen, RGB - Red, Green, Blue
        # screen.blit(test_surface,(200,250)) 
        pygame.display.update()
        clock.tick(60) # 60 frames per second