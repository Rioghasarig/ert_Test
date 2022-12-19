import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Computes an interpolation for a function f:R^2 -> R over a grid from a sample
# of points with known values. 
def interp2d(xmin, xmax, nx,
             ymin, ymax, ny,
             xs, ys, zs):

    assert len(xs.shape) == 1, "Inputs must be one-dimensional arrays"
    assert xs.size >= 2, "Interpolation requires at least two points"
    assert xs.size == ys.size and ys.size == zs.size, \
        "Inputs must be the same size"

    P = np.transpose(np.array([xs,ys]))
    V = np.linalg.norm(P[None,:,:] - P[:,None,:],axis=-1)
    a = np.linalg.solve(V,zs)

    x = np.linspace(xmin, xmax, nx)
    y = np.linspace(ymin, ymax, ny)
    xv,yv = np.meshgrid(x,y)

    X = xv[:,:,None] - xs
    Y = yv[:,:,None] - ys

    F = np.dot(np.sqrt(np.square(X) + np.square(Y)),a)
    return F
    

# Interpolate and plot the given example
xmin = 121.0
xmax = 131.0
nx = 70

ymin = 10.0
ymax = 16.0
ny = 50

xs = np.array([121.39,126.19,130.27,127.42,126.14,125.96,
              12315,130.5,129.08,122.74])

ys = np.array([13.51, 12.02, 13.11, 10.09, 15.33, 14,
               10.88, 11.18, 15.78, 15.82])

zs = np.array([1.494, 1.934, 2.148, 9.155, 2.221, 8.1,
               2.039, 1.916, 3.729, 7.137])


F = interp2d(xmin, xmax, nx,
             ymin, ymax, ny,
             xs, ys, zs)

#Flip F vertically so that y axis increases from bottom to top
F = F[np.arange(ny-1,-1,-1),:]

xticks = np.arange(xmin,xmax+2,2);
xlocs = [nx*(v-xmin)/(xmax-xmin) for v in xticks]
xticks = [format(v,".2f") for v in xticks]
plt.xticks(xlocs, xticks)

yticks = np.arange(ymin,ymax+1,1);
ylocs = [ny - ny*(v-ymin)/(ymax-ymin) for v in yticks]
yticks = [format(v,".2f") for v in yticks]
plt.yticks(ylocs, yticks)

plt.imshow(F)
plt.show()
