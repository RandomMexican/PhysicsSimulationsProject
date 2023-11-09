# made using this tutorial
# https://www.youtube.com/watch?v=cRWg2SWuXtM

import time
import pygame
import numpy as np

# colors that are going to be re used
background_color = (10,10,10)
Grid_color = (40,40,40)
change_color = (170,170,170)
Alive_color = (255,255,255)


def update(screen,cells,size, with_progress =False):
    updated_cells = np.empty((cells.shape[0],cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        # calculates the cells that are alive
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row,col]
        color = background_color if cells[row,col] == 0 else Alive_color

        if cells[row,col] == 1:
            if alive < 2 or alive >3:
                if with_progress:
                    color = change_color
            elif 2 <= alive <=3:
                updated_cells[row,col] = 1
                if with_progress:
                    color = Alive_color

        else:
            if alive == 3:
                updated_cells[row,col] = 1
                if with_progress:
                    color = Alive_color
        
        pygame.draw.rect(screen, color, (col * size, row * size, size -1, size -1))

    return updated_cells