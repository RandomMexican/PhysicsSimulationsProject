# made using this tutorial
# https://www.youtube.com/watch?v=cRWg2SWuXtM

import time
import pygame
import numpy as np

# colors that are going to be re used
background_color = (10,10,10)
Grid_color = (40,40,40)
# color if about to die
change_color = (170,170,170)
# color if alive
Alive_color = (255,255,255)

# func that applies game rules and updates cells
def update(screen,cells,size, with_progress =False):

    updated_cells = np.zeros((cells.shape[0],cells.shape[1]))

    
    for row, col in np.ndindex(cells.shape):
        # calculates the cells that are alive
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row,col]
        # default color
        color = background_color if cells[row,col] == 0 else Alive_color

        if cells[row,col] == 1:
            # living cell dies if too little or too many neighbors
            if alive < 2 or alive >3:
                if with_progress:
                    color = change_color
            # living cell stays alive if just enough neighbors
            elif 2 <= alive <=3:
                updated_cells[row,col] = 1
                if with_progress:
                    color = Alive_color
        
        #  brings a cell to life if dead cell is surrounded by 3 alive cells
        else:
            if alive == 3:
                updated_cells[row,col] = 1
                if with_progress:
                    color = Alive_color
        
        pygame.draw.rect(screen, color, (col * size, row * size, size -1, size -1))

    return updated_cells

def main():
    pygame.init()

    screen = pygame.display.set_mode((800,600))

    cells = np.zeros((60,80))
    screen.fill(Grid_color)
    update(screen,cells,10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                # depending on the value of running it either starts or ends/pauses the sim
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen,cells,10)

                    pygame.display.update()
            # changes a cell to alive if clicked
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1]// 10, pos[0] // 10] = 1
                update(screen,cells,10)
                pygame.display.update()

        screen.fill(Grid_color)

        # update cells using the rules of the game
        if running:
            cells = update(screen,cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == '__main__':
    main()
