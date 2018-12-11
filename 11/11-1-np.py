#!/usr/bin/python3

import numpy as np

cells = 300
serial = 2694

def powerlevel(x, y):
    rackid = x + 11
    return (rackid * (y + 1) + serial) * rackid

grid = ((np.fromfunction(powerlevel, (cells, cells), dtype=int) % 1000) // 100) - 5
sums = np.apply_over_axes(
        lambda a, axis: np.apply_along_axis(
            lambda a: a[0:cells-2] + a[1:cells-1] + a[2:cells],
            axis,
            a),
        grid,
        (0, 1))
answer = np.unravel_index(np.argmax(sums), sums.shape)
print(answer[1] + 1, answer[0] + 1)
