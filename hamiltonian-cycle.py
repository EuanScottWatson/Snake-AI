class Path:
    def __init__(self, x, y):
        # The entire graph - a grid
        self.graph = [[0 for _ in range(x)] for _ in range(y)]
        # List of directions to take one after another
        self.path_dir = []
        # List of actual coordinates taken
        self.path_cor = []

    def check_valid(self, pos, current):
        # Must be left, right, up or down from current - i.e. 1 away
        if (abs(pos[0] - current[0]) + abs(pos[1] - current[1])) != 1:
            return False

        # Cannot already be visited
        if pos in self.path_cor:
            return False

        return True


def main():
    new = Path(3, 3)


main()
