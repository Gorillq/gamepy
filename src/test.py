import pygame
import numpy as np

#some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

MAP_SIZE = 32


class Game:
    W = 640
    H = 640
    SIZE = W, H

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Game.SIZE)
        pygame.display.set_caption("DnD")
        self.running = True


class Tile:
    def __init__(self, column, row, size=(20, 20), margin=1, spacing=1):
        self.column = column
        self.row = row
        self.size = size
        self.margin = margin
        self.spacing = spacing

class Character:
    def __init__(self, name, column, row):
        self.name = name
        self.column = column
        self.row = row
    def move(self, direction):
        if direction == "UP":
            if self.row > 0:
                if not self.collisioncheck("UP"):
                    self.row -= 1
        elif direction == "DOWN":
            if self.row < MAP_SIZE-1:
                if not self.collisioncheck("DOWN"):
                    self.row += 1
        elif direction == "LEFT":
            if self.column > 0:
                if not self.collisioncheck("LEFT"):
                    self.column -= 1
        elif direction == "RIGHT":
            if self.column < MAP_SIZE-1:
                if not self.collisioncheck("RIGHT"):
                    self.column += 1
        Map.update()