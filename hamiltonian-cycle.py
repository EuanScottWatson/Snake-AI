import numpy as np

class Path:
    def __init__(self, x, y):
        self.size = x*y
        # The entire graph - a grid
        self.graph = [[0 for _ in range(x)] for _ in range(y)]
        # List of directions to take one after another
        self.path_dir = []
        # List of actual coordinates taken
        self.path_cor = []

        self.current = np.array([0, 0])

    def check_valid(self, pos, current):
        # Must be left, right, up or down from current - i.e. 1 away
        if (abs(pos[0] - current[0]) + abs(pos[1] - current[1])) != 1:
            return False

        # Cannot already be visited
        if pos in self.path_cor:
            return False

        return True

    def solve(self):
        # If all edges aren't included then continue
        # Check final and first are next to each other
        # Pick random adjacent square
        # Check if it's valid
        # Add if is
        # Continue
        # If not valid, add next neighbour
        # If no neighbours then pop and go back one
        pass


def main():
    new = Path(3, 3)


main()
