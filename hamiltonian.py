# The algorithm will work by having the grid be 0 to (w*h) with 0 in top left in one long array
# A grid of (m x n) can only be Hamiltonian iff m OR n is even and m,n > 1
# To clarify: m = Rows, n = Columns
# If m is even, snake right to left
# If n is even, snake down and up


def getXY(n, w):
    x = n % w
    y = n // w
    return x, y


def getLinear(x, y, w):
    return y * w + x


class Path:
    def __init__(self, w, h):
        # The linear number of each member in the path
        self.path = self.create_path(h, w)

    def create_path(self, m, n):
        if (m % 2 == 0) and (n % 2 == 0):
            print("No Hamiltonian cycle exists")
        if m % 2 == 0:
            return self.left_right_path(m, n)
        else:
            return self.up_down_path(m, n)

    def left_right_path(self, m, n):
        path = [0]
        for j in range(m):
            for i in range(1, n, 1):
                if j % 2 == 0:
                    path.append(getLinear(i, j, n))
                else:
                    path.append(getLinear((n - i), j, n))

        for j in range(m - 1, -1, -1):
            path.append(getLinear(0, j, n))

        return path

    def up_down_path(self, m, n):
        path = [0]
        for i in range(n):
            for j in range(1, m, 1):
                if i % 2 == 0:
                    path.append(getLinear(i, j, n))
                else:
                    path.append(getLinear(i, (m - j), n))

        for i in range(n - 1, -1, -1):
            path.append(getLinear(i, 0, n))

        return path
