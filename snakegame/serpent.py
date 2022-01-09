"""
model author: Jubril Ayomide Ajao
This module manages the snake object"""
import pygame


class Boa(object):
    """The Boidae, commonly known as boas or boids, are a family of nonvenomous snakes primarily found in the Americas,
    as well as Africa, Europe, Asia, and some Pacific Islands. Boas include some of the world's largest snakes,
    with the green anaconda of South America being the heaviest and second-longest snake known."""
    def __init__(self, screen):
        self.size = (20, 20)  # width, height
        # head position
        self.x, self.y = (int(screen[0] / 2), int(screen[1] / 2))

        # [[310, 270], [330, 270], [350, 270]]
        self.body_boa = [[self.x - 20 * i, self.y] for i in range(2, -1, -1)]
        # since the heading direction at the beginning is LEFT the head position
        # have to be self.head[0], which is [310,270] according to the loop
        self.head = [self.body_boa[0][0], self.body_boa[0][1]]
        self.dir = [
            pygame.K_LEFT,
            pygame.K_RIGHT,
            pygame.K_UP,
            pygame.K_DOWN,
        ]
        self.screen = pygame.display.set_mode(screen)
        self.color = (150, 150, 150)  # GRAY
        self.heading = "LEFT"
        self.change_heading = self.heading
        self.move_per_part = 20

    def check_key_press(self, event):
        """Manage changes in direction when any key in dir is pressed"""
        if event == pygame.K_LEFT:
            self.change_heading = "LEFT"
        elif event == pygame.K_RIGHT:
            self.change_heading = "RIGHT"
        elif event == pygame.K_DOWN:
            self.change_heading = "DOWN"
        elif event == pygame.K_UP:
            self.change_heading = "UP"

    def movement(self):
        """Coordinates the movement of the serpent according to the direction
        The heading of the serpent can not change to the opposite direction
        Eg:
        When heading to left, the serpent cannot change direction to right.
        Means in order to change direction, the serpent have to make a whole turn"""
        if self.change_heading == 'LEFT' and self.heading != 'RIGHT':
            self.heading = 'LEFT'
        elif self.change_heading == 'RIGHT' and self.heading != 'LEFT':
            self.heading = 'RIGHT'
        elif self.change_heading == 'DOWN' and self.heading != 'UP':
            self.heading = 'DOWN'
        elif self.change_heading == 'UP' and self.heading != 'DOWN':
            self.heading = 'UP'

        if self.heading == "LEFT":
            self.head[0] -= self.move_per_part
        elif self.heading == "RIGHT":
            self.head[0] += self.move_per_part
        elif self.heading == "UP":
            self.head[1] -= self.move_per_part
        elif self.heading == "DOWN":
            self.head[1] += self.move_per_part

        self.body_boa.insert(0, list(self.head))
        self.body_boa.pop()  # default is -1

        # display the list of coordinates
        for pos in self.body_boa:
            pygame.draw.rect(self.screen, self.color, pygame.Rect((pos[0], pos[1]), self.size))

    def detect_wall(self):
        """Detect if the x or y value of the first part of the serpent hit the wall (boundaries of the screen)
        The upper-left corner of the screen starts with the coordinates (0,0) width(x) and height(y).
         Due to calculation/process order the serpent hits the wall starting from the upper edge [-10, 710, 550, -10]"""
        width = self.screen.get_width()
        height = self.screen.get_height()
        if self.body_boa[0][0] <= -20 or self.body_boa[0][0] >= width+20:
            return True
        if self.body_boa[0][1] <= -20 or self.body_boa[0][1] >= height+20:
            return True

    def __str__(self):
        string_rep = f"Type: Boa\n" \
                     f"Start length: 60x20\n" \
                     f"Favor Food: Humans\n" \
                     f"Living: Austria"
        return string_rep
