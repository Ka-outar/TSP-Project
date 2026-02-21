import numpy as np

class TSPInstance:
    def __init__(self, coords):
        self.coords = np.array(coords)
        self.n = len(coords)
        self.dist_matrix = self._compute_matrix()

    def _compute_matrix(self):
        matrix = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(self.n):
                matrix[i, j] = np.sqrt(np.sum((self.coords[i] - self.coords[j])**2))
        return matrix

    def total_distance(self, tour):
        distance = 0
        for i in range(len(tour)):
            distance += self.dist_matrix[tour[i-1], tour[i]]
        return distance