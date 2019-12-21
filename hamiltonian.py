import numpy as np
import random


# The algorithm will work by having the grid be 0 to (w*h) with 0 in top left in one long array
# A grid of (m x n) can only be Hamiltonian iff m OR n is even and m,n > 1


def getXY(n, w):
    x = n % w
    y = n // w
    return x, y


def getLinear(x, y, w):
    return y * w + x


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbours = []


class Graph:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.size = w * h
        self.cells = []

    def initialise_cells(self):
        # Initialises all the cells
        for i in range(self.size):
            x, y = getXY(i, self.width)
            self.cells.append(Cell(x, y))

    def initialise_neighbours(self):
        for cell in self.cells:
            # Get the linear value for each neighbour
            left = getLinear(cell.x - 1, cell.y, self.width)
            right = getLinear(cell.x + 1, cell.y, self.width)
            up = getLinear(cell.x, cell.y - 1, self.width)
            down = getLinear(cell.x - 1, cell.y + 1, self.width)

            # If in range, add the relevent cells to the neighbours list
            if 0 <= left < self.size:
                cell.neighbours.append(self.cells[left])
            if 0 <= right < self.size:
                cell.neighbours.append(self.cells[right])
            if 0 <= up < self.size:
                cell.neighbours.append(self.cells[up])
            if 0 <= down < self.size:
                cell.neighbours.append(self.cells[down])


class Path:
    def __init__(self, w, h):
        # Get the graph set up
        self.graph = Graph(w, h)
        self.graph.initialise_cells()
        self.graph.initialise_neighbours()

        # The linear number of each member in the path
        self.path = []
