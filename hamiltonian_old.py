import numpy as np
import random


class Path:
    def __init__(self, x, y):
        self.size = x * y
        self.x = x
        self.y = y
        # The entire graph - a grid
        self.graph = [[0 for _ in range(x)] for _ in range(y)]
        # List of directions to take one after another
        self.path_dir = []
        # List of actual coordinates taken
        self.path_cor = []
        self.do_not_visit = [np.array([0, 0])]

        self.current = np.array([0, 0])
        self.back_track_levels = [[-1 for _ in range(x)] for _ in range(y)]
        self.back_track_level = 0

    def check_point(self, check, list):
        for point in list:
            if np.array_equal(point, check):
                return False
        return True

    def get_neighbours(self):
        neighbours = []
        neighbouring_cells = [np.array([-1, 0]), np.array([1, 0]), np.array([0, -1]), np.array([0, 1])]
        for neighb in neighbouring_cells:
            potential = self.current + neighb
            if self.check_point(potential, self.path_cor) and (0 <= potential[0] < self.x) and\
                    (0 <= potential[1] < self.y) and (self.back_track_level != self.back_track_levels[potential[1]][potential[0]]):
                neighbours.append(potential)

        if neighbours:
            return neighbours
        return False

    def complete(self):
        if len(self.path_cor) >= 2:
            if (abs(self.path_cor[0][0] - self.path_cor[-1][0]) + abs(self.path_cor[0][1] - self.path_cor[-1][0])) != 1 and \
                    len(self.path_cor) == self.size:
                return True
        return False

    def solve(self):
        pass

