"""model author:
Snake game made with pygame
"""

import pygame


class App:
    def __init__(self):
        self._game_active = True
        self.game_board = None
        self.size = self.weight, self.height = 640, 480
        self.caption = None

    def on_init (self):
        pygame.init()
        self.game_board = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self._caption = pygame.display.set_caption("Snake - eat em all")
        self._game_active = True

    #chek if user hits the Quit-button
    def on_event (self, event):
        if event.type == pygame.QUIT:
            self._game_active = False

            #add events, like hitting buttons etc.

    def on_loop (self):
        pass

        #computes changes in the game. movements of snake etc 

    def on_render (self):
        pass

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
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()

