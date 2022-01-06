"""model author:
Snake game made with pygame
"""

import pygame

# constant color dark-green
"""Color palette form: https://www.rapidtables.com/web/color/green-color.html"""
GREEN = (0, 100, 0)


class App:
    def __init__(self):
        self._game_active = True
        self.game_board = None
        self.size = [640, 480]
        self.caption = None

    def on_init(self):
        """initialize pygame and all necessary settings"""
        pygame.init()
        # the display/screen has Surface methods
        self.game_board = pygame.display.set_mode(self.size)
        # if no rect is specified, the color is applied to the whole screen
        self.game_board.fill(GREEN)
        pygame.display.set_caption("Snake - eat em all")
        # displays the whole thing, with changes etc.
        pygame.display.update()

        # self._game_active = True

    # check if user hits the Quit-button
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._game_active = False

            # add events, like hitting buttons etc.

    def on_loop(self):

        pass

        # Compute changes in the game. movements of snake etc

    def on_render(self):
        pass

        # print out the screen graphic

    def on_cleanup(self):
        """In order to properly quit the game"""
        pygame.quit()

    def on_execute(self):
        if not self.on_init():
            self._game_active == False

        # game loop
        while self._game_active:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
        # quit the game
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
