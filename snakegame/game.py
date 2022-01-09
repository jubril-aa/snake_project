"""model author:
Snake game made with pygame
"""

import pygame
import random
from snakegame.serpent import Boa

# GAME CONSTANTS
"""Color palette form: https://www.rapidtables.com/web/color/green-color.html"""
GREEN = (0, 100, 0)
GAME_SPEED = 10


class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random.randint(20, self.width - 20)
        self.y = random.randint(20, self.height - 20)


class App:
    orange = (0xFF, 0x8C, 0x00)

    def __init__(self):
        self.game_active = True
        self.game_board = None
        self.width = 700
        self.height = 540
        self.size = [self.width, self.height]
        self.clock = pygame.time.Clock()
        self.food = Food(self.width, self.height)
        # create snake
        self.snake = Boa(self.size)

        # Test object

    def on_init(self):
        """initialize pygame and all necessary settings"""
        pygame.init()
        # the display/screen has Surface methods
        self.game_board = pygame.display.set_mode(self.size)
        # if rect as argument is specified, the color is applied to the whole screen
        self.game_board.fill(GREEN)
        pygame.display.set_caption("Snake - eat em all")
        # displays the whole thing, with changes etc.
        self.clock.tick(GAME_SPEED)

    def register_quit(self, event):
        """check if user hits the Quit-button"""
        if event.type == pygame.QUIT:
            self.game_active = False

            # add events, like hitting buttons etc.

    def on_loop(self, event):
        """Runs everything when the game is active"""
        # snake behaviour
        if event.type == pygame.KEYDOWN:
            if event.key in self.snake.dir:
                self.snake.check_key_press(event.key)

        # Compute changes in the game. movements of snake etc

    def on_render(self, food):
        # 10 10 is the size of the food
        pygame.draw.rect(self.game_board, self.orange, pygame.Rect(self.food.x, self.food.y, 10, 10))
        # pygame.display.update()

        # print out the screen graphic

    def on_cleanup(self):
        """In order to properly quit the game"""
        # TODO: database stuff
        pygame.quit()

    def on_execute(self):
        """This is where the game come to life
        This loop is responsible for tasks such as checking for events (such as keyboard events or collision),
        moving objects, updating the display and eventually ending the game.
        """

        while self.game_active:  # True
            self.on_init()
            # event.get() collect every event that occurs
            for event in pygame.event.get():
                # check if the while loop should stop
                self.register_quit(event)
                self.on_loop(event)

                # all things the game should register during the while loop is true
            self.snake.movement()
            self.on_render(self.food)
            pygame.display.update()
            if self.snake.detect_wall():
                self.game_active = False

        # quit the game
        self.on_cleanup()


#
# if __name__ == "__main__":
#     theApp = App()
#     theApp.on_execute()

# play_snake = App()
