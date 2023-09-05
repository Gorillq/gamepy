import pygame as pg
import sys
import numpy as np
#from src import settings

#some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

MAP_SIZE = 32

#keys
# UP = pg.K_UP
# DOWN = pg.K_DOWN
# LEFT = pg.K_LEFT
# RIGHT = pg.K_RIGHT

#screen
SIZE = [255, 255]
W = 20
H = 20
MARGIN = 5

pg.init()
pg.display.set_caption("Gorillascroller")
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()
# back = pg.image.load("resources/background.jpg")
# grid = []
# for column in range(10):
#     grid.append([])
# for row in range(10):
#     grid[row].append(0)

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False


    screen.fill('BLACK')

    # for row in range(10):
    #     for column in range(10):
    #         color = WHITE
    #         if grid[row][column] == 1:
    #             color = RED
    #         pg.draw.rect(screen)


    pg.display.flip()

    clock.tick(30)

pg.quit()
sys.exit()


