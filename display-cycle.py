import pygame, os
import numpy as np
from pygame.locals import *
from hamiltonian import *


class Game:
    def __init__(self, n, m):
        self.path = Path(m, n)
        self.w = m
        self.h = n

    def display(self, screen):
        for j in range(self.h):
            for i in range(self.w):
                pygame.draw.circle(screen, (0, 0, 0), (60 * i + 30, 60 * j + 30), 15, 1)

        for i in range(self.h):
            pygame.draw.line(screen, (0, 0, 0), (0, 60 * i), (self.w * 60, 60 * i), 1)
        for i in range(self.w):
            pygame.draw.line(screen, (0, 0, 0), (60 * i, 0), (60 * i, self.h * 60), 1)

        for i in range(1, len(self.path.path), 1):
            x1, y1 = getXY(self.path.path[i - 1], self.w)
            x2, y2 = getXY(self.path.path[i], self.w)

            pygame.draw.line(screen, (0, 0, 0), (x1 * 60 + 30, y1 * 60 + 30), (x2 * 60 + 30, y2 * 60 + 30))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True

    def display_screen(self, screen):
        screen.fill((255, 255, 255))

        self.display(screen)

        pygame.display.update()
        pygame.display.flip()

    def run_logic(self):
        pass


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Arcade Machine")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    n, m = 10, 15
    width, height = m * 60, n * 60

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    game = Game(n, m)

    while not done:
        done = game.events()
        game.run_logic()
        game.display_screen(screen)

        clock.tick(120)


if __name__ == "__main__":
    main()
