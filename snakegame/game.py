"""model author:
Snake game made with pygame
"""

import pygame
from snakegame.food import Food
from snakegame.serpent import Boa

# GAME CONSTANTS
"""Color palette form: https://www.rapidtables.com/web/color/green-color.html"""
GREEN = (0, 100, 0)
GAME_SPEED = 10


class App:

    def __init__(self):
        self.game_active = True
        self.game_board = None
        self.width = 700
        self.height = 540
        self.size = (self.width, self.height)
        self.clock = pygame.time.Clock()
        # create food
        self.food = Food(width=self.width, height=self.height, board=self.size)
        # create snake
        self.snake = Boa(self.size)
        self.points = 0

    @property
    def points(self):
        """Return the points made during the game"""
        return self._points

    @points.setter
    def points(self, points):
        """Set the points"""
        assert type(points) == int
        self._points = points

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

    def on_loop(self, event):
        """Runs everything when the game is active"""
        if event.type == pygame.KEYDOWN:
            if event.key in self.snake.dir:
                self.snake.check_key_press(event.key)

    def on_cleanup(self):
        """In order to properly quit the game"""
        # TODO: database stuff
        # TODO: Stuffs before quiting
        print("game over")
        print(self.points)

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
            # needs a Rect argument
            if self.snake.eat(self.food.rect_food):
                self.points += 1
                self.food.grow_new_food()
                self.snake.grow_boa()

            else:
                self.food.grow_food()

            pygame.display.update()
            if self.snake.detect_wall() or self.snake.bite_self():
                self.game_active = False

        self.on_cleanup()
