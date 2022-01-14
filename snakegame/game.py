"""model author: Peter Pernhaupt, Florian Weiß, Jubril Ayomide Ajao
Snake game made with pygame
"""

import pygame
from snakegame.food import Food
from snakegame.serpent import Boa
import time
from snakegame.after_game import GameOver

pygame.font.init()

# GAME CONSTANTS
"""Color palette form: https://www.rapidtables.com/web/color/green-color.html"""
GREEN = (0, 100, 0)
WHITE = (255, 255, 255)
GAME_SPEED = 10
GAME_FONT = pygame.font.Font("freesansbold.ttf", 24)


class App:

    def __init__(self):
        self.game_active = True
        self.game_board = None
        self.width = 700
        self.height = 540
        self.size = (self.width, self.height)
        pygame.init()
        self.game_board = pygame.display.set_mode(self.size)
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

    def show_points(self):
        """Shows the current points on the top"""
        self.current_points = GAME_FONT.render("Score: %s" % self.points, True, WHITE, GREEN)
        self.game_board.blit(self.current_points, (10, 10))

    def on_init(self):
        """initialize pygame and all necessary settings"""
        self.game_board.fill(GREEN)
        pygame.display.set_caption("Snake - eat em all")
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
        """In order to properly quit the game after game actions"""

        # Displays Game over at the center of the screen
        pygame.display.set_caption("Game over")
        game_over_font = pygame.font.SysFont("didot.ttc", 72, bold=True)
        game_over_text = game_over_font.render("GAME OVER", True, WHITE)  # a Surface
        rect = game_over_text.get_rect()
        rect.center = (320, 240)
        self.game_board.blit(source=game_over_text, dest=rect)  # a Rect
        pygame.display.update()

        # wait two seconds before user can enter their username
        time.sleep(2)

        game_over = GameOver(self.size)

        # TODO: save points and username into database

        print("game over")
        print(self.points)
        print(game_over.text)
        pygame.quit()

    def on_execute(self):
        """This is where the game come to life
        This loop is responsible for tasks such as checking for events (such as keyboard events or collision),
        moving objects, updating the display and eventually ending the game.
        """
        while self.game_active:  # True
            self.on_init()
            self.show_points()
            # event.get() collect every event that occurs
            for event in pygame.event.get():
                # check if the while loop should stop
                self.register_quit(event)
                self.on_loop(event)

            # all things the game should register during the while loop is true
            self.snake.movement()
            # needs a Rect argument
            if self.snake.eat(self.food.rect_food):
                self.points += 10
                self.food.grow_new_food()
                self.snake.grow_boa()
            else:
                self.food.grow_food()

            pygame.display.update()
            if self.snake.detect_wall() or self.snake.bite_self():
                self.game_active = False

        self.on_cleanup()
