import pygame, os
import random
from pygame.locals import *
from hamiltonian import *


class Game:
    def __init__(self, n, m):
        # Setup Stuff
        self.path = Path(m, n)
        self.w = m
        self.h = n

        # Snake Stuff
        self.pointer = 0
        self.snake = [[0, 0]]
        self.new_body = False
        self.food = self.new_food()

    def display(self, screen):
        for body_cor in self.snake:
            body = pygame.Rect(body_cor[0]*60 + 7, body_cor[1]*60 + 7, 46, 46)
            if body_cor == self.snake[0]:
                pygame.draw.rect(screen, (1, 50, 32), body, 0)
            else:
                pygame.draw.rect(screen, (0, 255, 0), body, 0)

        for j in range(self.h):
            for i in range(self.w):
                if [i, j] == self.food:
                    pygame.draw.circle(screen, (255, 0, 0), (60 * i + 30, 60 * j + 30), 15, 0)
                    pygame.draw.circle(screen, (0, 0, 0), (60 * i + 30, 60 * j + 30), 15, 1)

        for i in range(self.h):
            pygame.draw.line(screen, (0, 0, 0), (0, 60 * i), (self.w * 60, 60 * i), 1)
        for i in range(self.w):
            pygame.draw.line(screen, (0, 0, 0), (60 * i, 0), (60 * i, self.h * 60), 1)

        '''
        for i in range(1, len(self.path.path), 1):
            x1, y1 = getXY(self.path.path[i - 1], self.w)
            x2, y2 = getXY(self.path.path[i], self.w)

            pygame.draw.line(screen, (0, 0, 0), (x1 * 60 + 30, y1 * 60 + 30), (x2 * 60 + 30, y2 * 60 + 30))
        '''

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                if event.key == K_SPACE:
                    self.add_body()

    def display_screen(self, screen):
        screen.fill((255, 255, 255))

        self.display(screen)

        pygame.display.update()
        pygame.display.flip()

    def check_food(self):
        if self.food == self.snake[0]:
            self.food = self.new_food()
            self.add_body()

    def new_food(self):
        if len(self.snake) != (self.w*self.h):
            food = self.snake[0]
            while food in self.snake:
                food = [random.randint(0, self.w-1), random.randint(0, self.h-1)]
            return food
        else:
            return [0, 0]

    def add_body(self):
        self.new_body = True

    def run_logic(self):
        if len(self.snake) != (self.w*self.h)+1:
            self.check_food()
            self.pointer = (self.pointer + 1) % len(self.path.path)
            x, y = getXY(self.path.path[self.pointer], self.w)
            tail = self.snake[-1]
            if len(self.snake) > 1:
                for i in range(len(self.snake)-1, 0, -1):
                    self.snake[i] = self.snake[i-1]
            self.snake[0] = [x, y]
            if self.new_body:
                self.snake.append(tail)
                self.new_body = False


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Arcade Machine")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    n, m = 9, 22
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
