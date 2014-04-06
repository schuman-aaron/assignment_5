import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
TAN = (250, 230, 140)
GREY = (200,200,200)

def remove_blocks(mpos, the_grid, update_pos, screen):
    x = mpos[0]
    y = mpos[1]
    #the position the user clicked on is not empty and within boundary
    if the_grid.pos[x][y].block != 'None' and y>0 and x<len(the_grid.pos) and x>0 and y<len(the_grid.pos[0]):
        #that position now contains nothing
        the_grid.pos[x][y].block = 'None'
        #change in block type could require updating of other blocks
        update_pos.append([x,y-1])
        update_pos.append([x+1,y-1])
        update_pos.append([x-1,y-1])
        #set density
        the_grid.pos[x][y].density = 0
        #change color
        screen.set_at((x,y), BLACK)
    return update_pos
