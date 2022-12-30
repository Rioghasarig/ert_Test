from random import randint
from boxfit_ffdh import *
import numpy as np
import itertools
def boxfit(container_dims, packages):
    fill_mask = np.zeros(container_dims)
    used = []
    positions = []
    vol = 0
    for i,package in enumerate(packages):
        for pos in itertools.product(range(0,container_dims[0]),
                                     range(0,container_dims[1]),
                                     range(0,container_dims[2])):
            #Check if the package fits in the position
            if pos[0] + package[0] >= container_dims[0]:
                continue
            if pos[1] + package[1] >= container_dims[1]:
                continue
            if pos[2] + package[2] >= container_dims[2]:
                continue

            if np.sum(fill_mask[pos[0]:pos[0]+package[0],
                                pos[1]:pos[1]+package[1],
                                pos[2]:pos[2]+package[2]]) > 0:
                continue
            
            fill_mask[pos[0]:pos[0]+package[0],
                      pos[1]:pos[1]+package[1],
                      pos[2]:pos[2]+package[2]] = 1
            used.append(i)
            positions.append(pos)
            vol = vol + package[0]*package[1]*package[2]            
            break
            

    return used,positions,(1.0*vol)/(container_dims[0]*container_dims[1]*container_dims[2])

#container_dims = [25, 56, 18]


"""packages = [[9, 38, 4],
            [8, 39, 4],
            [8, 39, 4],
            [8, 52, 4],
            [24, 23, 14],
            [12, 12, 7],
            [16, 21, 11],
            [15, 29, 10],
            [24, 36, 10],
            [21, 39, 7]]"""


# Sort the packages from largest to smallest

container_dims = [5,5,5]
packages = [(randint(1, 3), randint(1, 3), randint(1,3)) for _ in range(10)]

packages = sorted(packages, key=lambda x: -1*x[0] * x[1] * x[2])
used,positions,total_volume = boxfit(container_dims, packages)
print("Algorithm 1: ", total_volume)

vol,L = ffdh(container_dims, packages)
print ("Algorithm 2: ", vol, verify(container_dims,L))
