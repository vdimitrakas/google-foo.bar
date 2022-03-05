from collections import defaultdict
import numpy as np


def solution(dimensions, your_position, trainer_position, distance):
    x_dim, y_dim = dimensions
    a0, b0 = your_position
    x0, y0 = trainer_position

    hor = int(distance / x_dim) + 1
    ver = int(distance / y_dim) + 1

    shooter_dict = defaultdict(lambda: 1.001 * distance)
    trainer_dict = defaultdict(lambda: 1.001 * distance)

    for i in range(-hor, hor + 1):
        for j in range(-ver, ver + 1):

            x = x0 + i * x_dim + (i % 2) * (x_dim - 2 * x0)
            y = y0 + j * y_dim + (j % 2) * (y_dim - 2 * y0)

            distance_to_trainer = np.sqrt((x - a0) ** 2 + (y - b0) ** 2)

            if distance_to_trainer <= distance:
                rad_trainer = np.arctan2(x - a0, y - b0)
                trainer_dict[rad_trainer] = min(distance_to_trainer, trainer_dict[rad_trainer])

            a = a0 + i * x_dim + (i % 2) * (x_dim - 2 * a0)
            b = b0 + j * y_dim + (j % 2) * (y_dim - 2 * b0)

            distance_to_shooter = np.sqrt((a - a0) ** 2 + (b - b0) ** 2)
            if 0 < distance_to_shooter <= distance:
                rad_shooter = np.arctan2(a - a0, b - b0)
                shooter_dict[rad_shooter] = min(distance_to_shooter, shooter_dict[rad_shooter])

    ans = 0
    for k, v in trainer_dict.items():
        if v < shooter_dict[k]:
            ans += 1

    return ans


if __name__ == '__main__':
    room1 = [[3, 2], [1, 1], [2, 1], 4]
    room2 = [[300, 275], [150, 150], [185, 100], 500]

    print(f'Solution of the first test case is {solution(*room1)}')
    print(f'Solution of the second test case is {solution(*room2)}')
