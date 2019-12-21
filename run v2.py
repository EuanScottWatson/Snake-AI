import pygame, os
import random
from pygame.locals import *
from hamiltonian import *


class Game:
    def __init__(self, n, m, cell_size):
        # Setup Stuff
        self.path = Path(m, n)
        self.w = m
        self.h = n
        self.cell_size = cell_size

        self.pause = False

        # Snake Stuff
        self.pointer = 0
        self.snake = [[0, 0]]
        self.new_body = False
        self.food = self.new_food()

    def display(self, screen):
        body_width = self.cell_size * 2 // 3
        gap = (self.cell_size - body_width) // 2
        for body_cor in self.snake:
            body = pygame.Rect(body_cor[0] * self.cell_size + gap, body_cor[1] * self.cell_size + gap, body_width,
                               body_width)
            if body_cor == self.snake[0]:
                pygame.draw.rect(screen, (1, 50, 32), body, 0)
            else:
                pygame.draw.rect(screen, (0, 255, 0), body, 0)

        for j in range(self.h):
            for i in range(self.w):
                if [i, j] == self.food:
                    pygame.draw.circle(screen, (255, 0, 0), (
                        self.cell_size * i + (self.cell_size // 2), self.cell_size * j + (self.cell_size // 2)),
                                       (self.cell_size // 4), 0)
                    pygame.draw.circle(screen, (0, 0, 0), (
                        self.cell_size * i + (self.cell_size // 2), self.cell_size * j + (self.cell_size // 2)),
                                       (self.cell_size // 4), 1)

        for i in range(self.h):
            pygame.draw.line(screen, (0, 0, 0), (0, self.cell_size * i), (self.w * self.cell_size, self.cell_size * i),
                             1)
        for i in range(self.w):
            pygame.draw.line(screen, (0, 0, 0), (self.cell_size * i, 0), (self.cell_size * i, self.h * self.cell_size),
                             1)

        '''
        for i in range(1, len(self.path.path), 1):
            x1, y1 = getXY(self.path.path[i - 1], self.w)
            x2, y2 = getXY(self.path.path[i], self.w)

            pygame.draw.line(screen, (0, 0, 0),
                             (x1 * self.cell_size + (self.cell_size // 2), y1 * self.cell_size + (self.cell_size // 2)),
                             (x2 * self.cell_size + (self.cell_size // 2), y2 * self.cell_size + (self.cell_size // 2)))
        '''

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                if event.key == K_SPACE:
                    self.run_logic()

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
        if len(self.snake) != (self.w * self.h):
            food = self.snake[0]
            while food in self.snake:
                food = [random.randint(0, self.w - 1), random.randint(0, self.h - 1)]
            return food
        else:
            return [0, 0]

    def add_body(self):
        self.new_body = True

    def valid_coordinates(self, coor):
        [x, y] = coor
        if (0 <= x < self.w) and (0 <= y < self.h):
            return True
        return False

    def get_neighbours(self, x, y):
        neighbours = []
        left = [x - 1, y]
        right = [x + 1, y]
        up = [x, y - 1]
        down = [x, y + 1]

        # If in range, add the relevant cells to the neighbours list
        if self.valid_coordinates(left):
            neighbours.append(getLinear(left[0], left[1], self.w))
        if self.valid_coordinates(right):
            neighbours.append(getLinear(right[0], right[1], self.w))
        if self.valid_coordinates(up):
            neighbours.append(getLinear(up[0], up[1], self.w))
        if self.valid_coordinates(down):
            neighbours.append(getLinear(down[0], down[1], self.w))

        return neighbours

    def check_food_body(self, s, e):
        if self.path.path.index(e) > self.path.path.index(getLinear(s[0], s[1], self.w)):
            for n in range(getLinear(s[0], s[1], self.w), e, 1):
                check = getXY(n, self.w)
                if self.food == check or check in self.snake:
                    return False
        else:
            for n in range(getLinear(s[0], s[1], self.w), len(self.path.path), 1):
                check = getXY(n, self.w)
                if self.food == check or check in self.snake:
                    return False
            for n in range(0, e, 1):
                check = getXY(n, self.w)
                if self.food == check or check in self.snake:
                    return False
        return True

    def new_head(self):
        [x, y] = self.snake[0]
        neighbours = self.get_neighbours(x, y)
        best = None
        dist = 0

        for neighb in neighbours:
            if self.path.path.index(neighb) > self.path.path.index(getLinear(x, y, self.w)) and self.check_food_body(
                    [x, y], neighb):
                if self.path.path.index(neighb) > self.path.path.index(getLinear(x, y, self.w)):
                    new_dist = self.path.path.index(neighb) - self.path.path.index(getLinear(x, y, self.w))
                    if new_dist > dist:
                        best = neighb
                else:
                    new_dist = len(self.path.path) - self.path.path.index(neighb) + self.path.path.index(
                        getLinear(x, y, self.w))
                    if new_dist > dist:
                        best = neighb

        if best:
            return getXY(best, self.w)
        else:
            self.pointer = (self.pointer + 1) % len(self.path.path)
            x, y = getXY(self.path.path[self.pointer], self.w)
            return [x, y]

    def run_logic(self):
        if not self.pause:
            if len(self.snake) != (self.w * self.h) + 1:
                self.check_food()
                head = self.new_head()
                tail = self.snake[-1]
                if len(self.snake) > 1:
                    for i in range(len(self.snake) - 1, 0, -1):
                        self.snake[i] = self.snake[i - 1]
                self.snake[0] = head
                if self.new_body:
                    self.snake.append(tail)
                    self.new_body = False


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Arcade Machine")

    os.environ['SDL_VIDEO_CENTERED'] = "True"

    n, m = 6, 5
    cell_size = 60
    width, height = m * cell_size, n * cell_size

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    game = Game(n, m, cell_size)

    while not done:
        done = game.events()
        #game.run_logic()
        game.display_screen(screen)

        clock.tick(3)


if __name__ == "__main__":
    main()
