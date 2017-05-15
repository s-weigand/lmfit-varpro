import numpy as np


def dot(e, c):
    res = np.empty((len(c), len(e)), dtype=np.float64)

    for x, t in iter_c_and_e(c, e):
        res[x, t] = np.dot(c[x][t, :], e[t][x, :].T)

    return res


def iter_c_and_e(c, e):
    for i in range(len(c)):
        for j in range(len(e)):
            yield i, j
