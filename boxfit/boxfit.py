from random import randint
from boxfit_ffdh import *
import numpy as np
import itertools

# Fills in the box using the First-Fit Decreasing Height Heursitic, adapted
# to work for the 3D case.

# Boxes are sorted in order of decreasing height. Boxes are added in order along
# the x-axis unti we come across a box that can no longer fit. We then move along
# the y-axis to add a new row of boxes.These steps are repeated until a full layer
# of boxes is completed at the bottom of the container. We then move up in the
# z-axis and repeat the process for a new layer. If box is ever too tall to fit
# into the container (at the current height level being filled) it is skipped over

def ffdh(container, boxes):
    sorted(boxes, key=lambda x: x[2])

    xpos = 0
    ypos = 0 
    zpos = 0

    box_idx = 0
    placements  = []
    maxY  = 0
    maxZ = 0
    vol = 0 
    while True:
        if box_idx >= len(boxes):
            break
        box = boxes[box_idx]
        if box[0] > container[0] or box[1] > container[1] or box[2] > container[2]:
            box_idx += 1
            continue        
        if xpos + box[0] <= container[0] and ypos + box[1] <= container[1] \
           and zpos + box[2] <= container[2]:
                # Record id, position, and dimensions of box used
                placements.append((box_idx,(xpos, ypos, zpos), box))
                vol += box[0]*box[1]*box[2]
                if box[1] > maxY:
                    maxY = box[1]
                if box[2] > maxZ:
                    maxZ = box[2]
                box_idx += 1
                xpos += box[0]
                
        # Start a new row of boxes if current row goes over the edge in the
        # x direction
        elif xpos + box[0] > container[0]:
            ypos = ypos + maxY            
            xpos = 0
            maxY = 0
            continue
        
        # Starts a new layer of boxes if current layer goes over the edge in the
        # y direction
        elif ypos + box[1] > container[1]:
            zpos += maxZ
            xpos = 0
            ypos = 0
            maxY = 0
            maxZ = 0
            continue

        # Skip boxes too tall to fit at the current height level
        elif zpos + box[2] > container[2]:
            box_idx += 1
            continue            
    return (1.0*vol/(container[0]*container[1]*container[2]),placements)

# Brute force implementation of the box fitting algorithm. Takes all boxes,
# sorted from largest to smallest and finds the first place they fit within
# the container. 
def boxfit(container_dims, packages):
    packages = sorted(packages, key=lambda x: -1*x[0] * x[1] * x[2])
    fill_mask = np.zeros(container_dims)
    vol = 0
    placements = []
    for box_idx,package in enumerate(packages):
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

            # Mark the area as used
            fill_mask[pos[0]:pos[0]+package[0],
                      pos[1]:pos[1]+package[1],
                      pos[2]:pos[2]+package[2]] = 1
            
            # Record the ID, position, and dimensions of box used
            placements.append((box_idx, (pos[0],pos[1],pos[2]),package))
            vol = vol + package[0]*package[1]*package[2]            
            break
            

    return ((1.0*vol)/(container_dims[0]*container_dims[1]*container_dims[2]), placements)

# Verify that the boxes are really non-overlapping
def verify(container, placements):
    fill_mask = np.zeros(container)
    for box_placement in placements:
        xpos,ypos,zpos = box_placement[1]
        dim_x,dim_y,dim_z = box_placement[2]
        if np.any(fill_mask[xpos:xpos+dim_x,ypos:ypos+dim_y,zpos:zpos+dim_z]):
            return False
        else:
            fill_mask[xpos:xpos+dim_x,ypos:ypos+dim_y,zpos:zpos+dim_z] = 1
    return True
 

def read_triples(filename):
    with open(filename, 'r') as file:
        container = tuple(map(int, file.readline().split()))
        packages = [tuple(map(int, line.split())) for line in file]
    return container, packages
                
container_dims, packages = read_triples("input.txt")

#container_dims = [20,20,20]
#packages = [(randint(1, 5), randint(1, 5), randint(1,5)) for _ in range(1000)]

total_volume,placements1 = boxfit(container_dims, packages)
print("Algorithm 1: ", total_volume, verify(container_dims,placements1))

vol,placements2 = ffdh(container_dims, packages)
print ("Algorithm 2: ", vol, verify(container_dims,placements2))

