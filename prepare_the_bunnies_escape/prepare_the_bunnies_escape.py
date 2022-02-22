import numpy as np


class DP:
    def __init__(self, map):
        self.map = np.array(map)
        self.width, self.height = self.map.shape

    def forward_solution(self, map, v):
        c = 0

        for m in range(self.width):
            for n in range(self.height):
                if (m, n) == (0, 0):
                    v[m, n] = 1
                if (map[m, n] > 0) or (not np.isnan(v[m, n])):
                    continue
                elif not np.isnan(v[m - 1, n]):
                    v[m, n] = 1 + v[m - 1, n]
                    c += 1
                elif not np.isnan(v[m, n - 1]):
                    c += 1
                    v[m, n] = 1 + v[m, n - 1]

        return v, c

    def backward_solution(self, map, v):
        c = 0

        for m in range(self.width - 1, -1, -1):
            for n in range(self.height - 1, -1, -1):

                if (map[m, n] > 0) or (not np.isnan(v[m, n])):
                    continue

                elif (self.width > m + 1) and (not np.isnan(v[m + 1, n])):
                    v[m, n] = 1 + v[m + 1, n]
                    c += 1
                elif (self.height > n + 1) and (not np.isnan(v[m, n + 1])):
                    v[m, n] = 1 + v[m, n + 1]
                    c += 1

        return v, c

    def values_matrix(self, map):
        c = 1
        v = np.nan * np.ones_like(map)
        while c > 0:
            v, _ = self.forward_solution(map, v)
            v, c = self.backward_solution(map, v)
        return v[self.width - 1, self.height - 1]

    def solution(self):
        ans = self.width * self.height + 1

        temp = self.values_matrix(self.map)
        if temp < ans:
            ans = temp

        for i in range(self.width):
            for j in range(self.height):
                if self.map[i, j] == 0:
                    continue
                tmap = self.map.copy()
                tmap[i, j] = 0
                temp = self.values_matrix(tmap)
                if temp < ans:
                    ans = temp

        return int(ans)


def solution(map):
    dp = DP(map)
    return dp.solution()
