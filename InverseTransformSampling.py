import numpy as np

def pdftocdf(x,y,p,shape):
    xs,ys = (shape[0]/np.max(x.flatten()),shape[1]/np.max(y.flatten()))
    px = np.sum(p,axis=1)
    px = np.cumsum(px)
    p = np.apply_along_axis(np.cumsum,0,p)
    p = np.apply_along_axis(np.cumsum,1,p)
    p = p/np.max(p.flatten())
    return (p,x*xs,y*ys,px/np.max(px.flatten()))

def samplecdf1(ux,uy,p,x,y,px): # no interpolation
    a1 = np.argmin(np.abs(px-ux))
    sel_x = x[0,:][a1]
    sel_y = y[:,0][np.argmin(np.abs(p[a1,:]/np.max(p[a1,:].flatten())-uy))]
    return sel_x,sel_y

def transformp(cn,p,x,y,shape):
    p,x,y,px = pdftocdf(x,y,p,shape)
    ans = []
    for i in range(cn):
        ans.append(samplecdf1(np.random.rand(),np.random.rand(),p,x,y,px))
    return ans

def gaussian(mx,my,sigmax,sigmay,corr=0,spacing=None,shape=None):
    mx = mx*shape[0]
    my = my*shape[1]
    if spacing is None:
        x = np.linspace(0,shape[0],1500)
        y = np.linspace(0,shape[1],1500)
    else:
        x = np.arange(0,shape[0],spacing)
        y = np.arange(0,shape[1],spacing)
    x,y = np.meshgrid(x,y)
    p = 1/(2*np.pi*sigmax*sigmay*np.sqrt(1-corr**2))*np.exp(-1/(2-2*corr**2)*((x-mx)**2/sigmax**2 + (y-my)**2/sigmay**2 - 2*corr*(x-mx)*(y-my)/sigmax/sigmay))
    return (p,x,y)