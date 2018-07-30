import numpy as np

def bordercalc(a,t,amin):
    m1 = a[amin]
    a = a.tolist()
    m2 = np.min(a[0:amin]+a[amin+1:len(a)])
    if m2 - m1 <= t:
        return True
    else:
        return False


def tessel_low_mem(clusters,shape,verbose=True,border=False,threshold=200):
    dist = np.zeros(shape[0:2], dtype=np.int16)
    for i in range(1,shape[0]+1):
        if verbose:
            print(str(int(i / shape[0] * 100)) + '% done \t\t\r', end='')
        for j in range(1,shape[1] + 1):
            subdists = (clusters[:, 0] - i) ** 2 + (clusters[:, 1] - j) ** 2
            clus = np.argmin(np.array(subdists))
            if border:
                if bordercalc(subdists, threshold, clus):
                    dist[i - 1, j - 1] = len(clusters[:,0]) + 1
                else:
                    dist[i - 1, j - 1] = clus
            else:
                dist[i - 1, j - 1] = clus
    return dist