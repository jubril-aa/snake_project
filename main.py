"""model author:
Snake game made with pygame
"""

import pygame
import random

# constant color dark-green for the background
"""Color palette form: https://www.rapidtables.com/web/color/green-color.html"""
GREEN = (0, 100, 0)


class Food:
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
        self.size = [self.width, self.height]
        self.caption = None
        self.clock = pygame.time.Clock()
        self.food = Food(self.width, self.height)

    def on_init(self):
        """initialize pygame and all necessary settings"""
        pygame.init()

        # the display/screen has Surface methods
        self.game_board = pygame.display.set_mode(self.size)
        # if rect as argument is specified, the color is applied to the whole screen
        self.game_board.fill(GREEN)
        pygame.display.set_caption("Snake - eat em all")
        # displays the whole thing, with changes etc.
        pygame.display.update()

    def on_event(self, event):
        """check if user hits the Quit-button"""
        self.game_board = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Snake - eat em all")
        self._game_active = True
        self.clock.tick(25)

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

    def on_render(self, food):
        # 20 20 is the size of the food
        pygame.draw.rect(self.game_board, self.orange, pygame.Rect(self.food.x, self.food.y, 20, 20))
        pygame.display.flip()

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
            self.on_render(self.food)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
