import numpy as np

def bordercalc(x,threshold,cn):
   if True in (-np.diff(np.sort(x,0)))<=threshold:
       return cn+1
   else:
       return np.argmin(x)


def tessel_fast(clusters,shape,verbose=True,border=False,threshold=200):
    if verbose:
        print("Loading Array of Indices")
    indices = np.indices((shape[0],shape[1]),dtype=np.int16).transpose([1,2,0])
    if verbose:
        print('Computing Distances.')
    indices = np.sum((clusters.transpose()[None,None,:,:]-indices[:,:,:,None])**2,axis=2)
    if not border:
        if verbose:
            print('Assigning Clusters.')
        return  np.apply_along_axis(np.argmin,2,indices)
    if verbose:
        print('Assigning Clusters and Border tags.')
    return np.apply_along_axis(lambda x: bordercalc(x,threshold,len(clusters)),2,indices)