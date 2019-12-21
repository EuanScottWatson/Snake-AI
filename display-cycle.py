import pygame, os
from pygame.locals import *
from hamiltonian_old import *


class Game:
    def __init__(self):
        self.graph = Path(10, 10)
        self.graph.solve()

    def display(self, screen):
        for j in range(10):
            for i in range(10):
                pygame.draw.circle(screen, (0, 0, 0), (60*i+30, 60*j+30), 15, 1)

        for i in range(10):
            pygame.draw.line(screen, (0, 0, 0), (0, 60*i), (600, 60*i), 1)
            pygame.draw.line(screen, (0, 0, 0), (60*i, 0), (60*i, 600), 1)

        if not self.graph.complete():
            self.graph.solve()

        if len(self.graph.path_cor) >= 2:
            for i in range(1, len(self.graph.path_cor), 1):
                pygame.draw.line(screen, (0, 0, 0), (self.graph.path_cor[i-1]*60 + np.array([30, 30])), (self.graph.path_cor[i]*60 + np.array([30, 30])), 1)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return True
                if event.key == K_SPACE:
                    self.graph.solve()

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

    width, height = 600, 600

    screen = pygame.display.set_mode((width, height))

    done = False
    clock = pygame.time.Clock()
    game = Game()

    while not done:
        done = game.events()
        game.run_logic()
        game.display_screen(screen)

        clock.tick(120)


if __name__ == "__main__":
    main()
