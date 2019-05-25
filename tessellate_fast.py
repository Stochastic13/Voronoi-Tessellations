import numpy as np
from multiprocessing import Pool, Process, Manager


def initfoo(data):
    global clus
    clus = data


def workerfoo(ind):
    subdists = (clus[:, 0] - ind[0]) ** 2 + (clus[:, 1] - ind[1]) ** 2
    return np.argmin(np.array(subdists))


def tessel_fast(clusters, shape, verbose=True, border=False, threshold=200):
    if verbose:
        print("Loading array of indices")
    indices = [(i, j) for i in range(shape[0]) for j in range(shape[1])]
    clus = None
    if verbose:
        print('Computing distances.')
    with Pool(initializer=initfoo, initargs=(clusters, )) as P:
        dist = np.array(P.map(workerfoo, indices, chunksize=100))
    dist = dist.reshape(shape[0:2])
    return dist
