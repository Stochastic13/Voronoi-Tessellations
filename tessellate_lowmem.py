import numpy as np


def bordercalc(a, t, amin):  # If drawing borders is True
    m1 = a[amin]  # Distance from the closest cluster center
    a = a.tolist()
    m2 = np.min(a[0:amin] + a[amin + 1:len(a)])  # Distance from the second closest cluster center.
    if m2 - m1 <= t:
        return True
    else:
        return False


def tessel_low_mem(clusters, shape, verbose=True, border=False, threshold=200):
    dist = np.zeros(shape[0:2], dtype=np.uint16)  # The 2D cluster membership array (up to 65536 clusters)
    for i in range(1, shape[0] + 1):
        if verbose:
            print(str(int(i / shape[0] * 100)) + '% done \t\t\r', end='')
        for j in range(1, shape[1] + 1):
            subdists = (clusters[:, 0] - i) ** 2 + (clusters[:, 1] - j) ** 2
            clus = np.argmin(np.array(subdists))
            if border:  # I am assuming the np.array() call above is just for my mental peace and serves no purpose
                if bordercalc(subdists, threshold, clus):
                    dist[i - 1, j - 1] = len(clusters[:, 0]) + 1  # Special index to identify borders
                else:
                    dist[i - 1, j - 1] = clus
            else:
                dist[i - 1, j - 1] = clus  # I can't see why I start i,j from 1, and then subtract 1 at the end.
                # But I am keeping it like this in hope that my past self had some rationale.
    return dist
