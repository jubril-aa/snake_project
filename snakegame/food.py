"""model author: Florian Weiß
Food of the serpent
"""

import random
import pygame

ORANGE = (0xFF, 0x8C, 0x00)


class Food:
    def __init__(self, **kwargs):
        self.rect = None
        self.width = kwargs["width"]
        self.height = kwargs["height"]
        self.board = pygame.display.set_mode(kwargs["board"])
        # food should stay in an acceptable distance from the wall
        self.x = random.randint(20, self.width - 20)
        self.y = random.randint(20, self.height - 20)
        self.color = ORANGE
        self.size = (10, 10)
        self.rect_food = pygame.Rect((self.x, self.y), self.size)

    def grow_food(self):
        """Allows to display the food until it got eaten"""
        self.rect = pygame.draw.rect(self.board, self.color, self.rect_food)
        return self.rect

    def grow_new_food(self):
        """Creates new random position for food"""
        x = random.randint(20, self.width - 20)
        y = random.randint(20, self.height - 20)
        self.rect_food = pygame.Rect((x, y), self.size)




