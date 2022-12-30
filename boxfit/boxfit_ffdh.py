from random import randint
import numpy as np

def ffdh(container, boxes):
    sorted(boxes, key=lambda x: x[0])

    xpos = 0
    ypos = 0 
    zpos = 0

    box_idx = 0
    L  = []
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
                L.append((box_idx,(xpos, ypos, zpos), box))
                vol += box[0]*box[1]*box[2]
                if box[1] > maxY:
                    maxY = box[1]
                if box[2] > maxZ:
                    maxZ = box[2]
                box_idx += 1
                xpos += box[0]
        elif xpos + box[0] > container[0]:
            ypos = ypos + maxY            
            xpos = 0
            maxY = 0
            continue
        elif ypos + box[1] > container[1]:
            zpos += maxZ
            xpos = 0
            ypos = 0
            maxY = 0
            maxZ = 0
            continue
        elif zpos + box[2] > container[2]:
            box_idx += 1
            continue            
    return (1.0*vol/(container[0]*container[1]*container[2]),L)

#boxes = [(randint(1, 3), randint(1, 3), randint(1,3)) for _ in range(10)] 

def verify(container, L):
    fill_mask = np.zeros(container)
    for box_placement in L:
        xpos,ypos,zpos = box_placement[1]
        dim_x,dim_y,dim_z = box_placement[2]
        if np.any(fill_mask[xpos:xpos+dim_x,ypos:ypos+dim_y,zpos:zpos+dim_z]):
            return False
        else:
            fill_mask[xpos:xpos+dim_x,ypos:ypos+dim_y,zpos:zpos+dim_z] = 1
    return True
#container = (5,5,5)
#vol,L = ffdh(container, boxes)
#print(vol, L)
#print(verify(container, L))
 

    
