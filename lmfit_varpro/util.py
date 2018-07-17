import numpy as np


def dot(e, c):
    dim1 = len(e)
    dim2 = c[0].shape[0]
    res = np.empty((dim1, dim2), dtype=np.float64)

    for i in range(len(c)):
        res[i, :] = np.dot(c[i], e[i])

    return res
