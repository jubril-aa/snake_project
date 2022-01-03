"""model author:
Snake game made with pygame
"""

import pygame
import random





class food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.randint(20, self.width - 20)
        self.y = random.randint(20, self.height - 20)


class App:

    orange = (0xFF, 0x8C, 0x00)


    def __init__(self):
        self._game_active = True
        self.game_board = None
        self.width = 640
        self.height = 480
        self.size = self.width, self.height
        self.caption = None
        self.clock = pygame.time.Clock()
        self.food = food(self.width, self.height)

    def on_init (self):
        pygame.init()
        self.game_board = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self.caption = pygame.display.set_caption("Snake - eat em all")
        self._game_active = True
        self.clock.tick(25)

    #chek if user hits the Quit-button
    def on_event (self, event):
    

        if event.type == pygame.QUIT:
            self._game_active = False

            #add events, like hitting buttons etc.

    def on_loop (self):
        pass

        #computes changes in the game. movements of snake etc 

    def on_render (self, food):
        pygame.draw.rect(self.game_board, self.orange, pygame.Rect(self.food.x, self.food.y, 20, 20)) #20 20 is the size of the food
        pygame.display.flip()


        #print out the screen graphic

        
    def on_cleanup(self):
        pygame.quit()


    def on_execute(self):
        if self.on_init () == False:
            self._game_active == False

        #game loop
        while (self._game_active):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render(self.food)
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

