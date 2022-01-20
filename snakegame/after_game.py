"""
module author: Jubril Ayomide Ajao
Update the whole game screen to let user
input their usernames and displays the top ten"""

import pygame
import time
from snakegame.scores_db import get_top, insert_score

GREEN = (0, 100, 0)
WHITE = (255, 255, 255)


class GameOver(object):
    """Game over class"""
    def __init__(self, size, points):
        self.size = size
        self.points = points
        self.text = "Write Username"
        self.to_continue = "Press Enter to continue"
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        # initialize new screen
        self.over()

    def display_ten(self):
        """Displays top ten"""
        username = self.text.strip()
        insert_score(username, self.points)

        pygame.display.set_caption("Top Ten")
        top_font = pygame.font.SysFont("didot.ttc", 60)
        top_text = top_font.render("TOP 10", True, WHITE)
        top_rect = top_text.get_rect()
        top_rect.center = (350, 60)
        self.screen.fill(GREEN)
        self.screen.blit(top_text, top_rect)

        dis = 120  # starting for the distance in between the players
        for num, value in enumerate(get_top(10), 1):
            player_font = pygame.font.SysFont("didot.ttc", 30)
            player_text = player_font.render(f"{num}.  {value['user']}    {value['points']}", True, WHITE)
            player_rect = player_text.get_rect()
            # for the alignment -> left align
            player_rect.topleft = (280, dis)
            self.screen.blit(player_text, player_rect)
            dis += 30
        pygame.display.update()

    def over(self):
        """Displays after game actions for user input"""
        # Tell user what to do
        next_font = pygame.font.SysFont("didot.ttc", 55)
        next_text = next_font.render(self.to_continue, True, WHITE)
        # get the rectangle of the text
        rect_next = next_text.get_rect()
        rect_next.center = (320, 80)

        font = pygame.font.SysFont("silom.ttf", 48)
        img = font.render(self.text, True, "white")

        rect = img.get_rect()
        rect.center = (320, 240)
        cursor = pygame.Rect(rect.topright, (3, rect.height))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if len(self.text) > 0:
                            self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    img = font.render(self.text, True, "white")
                    rect.size = img.get_size()
                    cursor.topleft = rect.topright

            self.screen.fill(GREEN)
            self.screen.blit(next_text, rect_next)
            self.screen.blit(img, rect)
            if time.time() % 1 > 0.5:
                pygame.draw.rect(self.screen, WHITE, cursor)
            pygame.display.update()

        self.display_ten()
