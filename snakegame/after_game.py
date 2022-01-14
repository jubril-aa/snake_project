"""
model author: Jubril Ayomide Ajao
Update the whole game screen to let user input their usernames """

import pygame
import time


GREEN = (0, 100, 0)
WHITE = (255, 255, 255)


class GameOver(object):
    """Game over class"""
    def __init__(self, size):
        self.size = size
        self.text = "Write Username"
        self.to_continue = "Press Enter to continue"
        # initialize new screen
        self.over()

    def over(self):
        """Displays after game actions for user input"""
        pygame.init()
        screen = pygame.display.set_mode(self.size)

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

            screen.fill(GREEN)
            screen.blit(next_text, rect_next)
            screen.blit(img, rect)
            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen, WHITE, cursor)
            pygame.display.update()

        pygame.quit()
