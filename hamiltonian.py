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

    def check_point(self, check, list):
        for point in list:
            if np.array_equal(point, check):
                return False
        return True

    def check_valid(self, pos, current):
        # Must be left, right, up or down from current - i.e. 1 away
        if (abs(pos[0] - current[0]) + abs(pos[1] - current[1])) != 1:
            return False

        # Cannot already be visited
        if pos in self.path_cor:
            return False

        return True

    def get_neighbours(self, current, path_cor):
        neighbours = []
        neighbouring_cells = [np.array([-1, 0]), np.array([1, 0]), np.array([0, -1]), np.array([0, 1])]
        for neighb in neighbouring_cells:
            potential = current + neighb
            if self.check_point(potential, self.path_cor) and (0 <= potential[0] < self.x) and\
                    (0 <= potential[1] < self.y) and not np.array_equal(potential, self.do_not_visit):
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
        # If all edges aren't included then continue
        # Check final and first are next to each other
        # Pick random adjacent square
        # Check if it's valid
        # Add if is
        # Continue
        # If not valid, add next neighbour
        # If no neighbours then pop and go back one
        #print(self.path_cor)
        neighbours = self.get_neighbours(self.current, self.path_cor)
        if not neighbours:
            self.do_not_visit.append(self.current)
            self.current = self.path_cor.pop()
            self.path_dir.pop()
            print("S:", self.current, self.do_not_visit)
        else:
            print("N: ", self.current, neighbours)
            self.do_not_visit = []
            next = random.choice(neighbours)
            self.path_dir.append(next - self.current)
            self.path_cor.append(self.current)
            self.current = next

