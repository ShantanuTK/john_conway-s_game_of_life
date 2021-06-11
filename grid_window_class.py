'''
to do
1) get_alive_nieghoburs function
2)conway_play function
''' 

from hashlib import new
import random
import pygame
from pygame.constants import APPFOCUSMOUSE
vec = pygame.math.Vector2
import colours
from cell_class import Cell
import copy
import sys

offsets = {
    "up": (0, -1),
    "upRight": (1, -1),
    "right": (1, 0),
    "downRight": (1, 1),
    "down": (0, 1),
    "downLeft": (-1, 1),
    "left": (-1, 0),
    "upLeft": (-1, -1)
}


class GridWindow():
    def __init__(self, backgroud, x, y, width, rows):
        self.background = backgroud
        self.pos = vec(x, y)
        self.width = width
        self.surface = pygame.Surface((self.width, self.width))
        self.rect = self.surface.get_rect()
        self.rows = rows
        self.rect.topleft = self.pos
        self.grid = self.make_grid()

        for rows in self.grid:
            for cell in rows:
                cell.get_neighbours(self.grid)

    def update(self):
        self.rect.topleft = self.pos
        for rows in self.grid:
            for cell in rows:
                cell.check_neighbours()


    def reset_grid(self):
        self.grid = self.make_grid()

    def grid_randomise(self):
        for row in self.grid:
            for cell in row:
                cell.random = random.choice((0, 1))
                if cell.random == 1:
                    cell.make_alive()
                else:
                    cell.make_dead()


    def click_cell(self, pos):
        gap = self.width // self.rows
        x, y = pos

        row = (y - 100) // gap
        column = (x - 50)  // gap

        if self.grid[row][column].alive:
            self.grid[row][column].alive = False
        else:
            self.grid[row][column].alive = True
        

    def make_grid(self):
        grid = []
        gap = self.width // self.rows
    
        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                grid[i].append(Cell(self.surface, i, j, gap, self.rows))
        
        return grid

    def draw_grid_lines(self):
        gap = self.width // self.rows

        for i in range(self.rows):
            pygame.draw.line(self.surface, colours.GRID_LINES, (0, i * gap), (self.width, i * gap))

            for j in range(self.rows):
                pygame.draw.line(self.surface, colours.GRID_LINES, (j * gap, 0), (j * gap, self.width))


    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

        self.draw_grid_lines()
        self.background.blit(self.surface, self.rect.topleft)

    def conway(self):
        newGrid = copy.copy(self.grid)
        for rows in self.grid:
            for cell in rows:
                cell.get_alive_neighbours()

        for r, rows in enumerate(self.grid):
            for c, cell in enumerate(rows):
                if cell.is_alive():
                    if cell.aliveNeighbours == 2 or cell.aliveNeighbours == 3:
                        newGrid[r][c].alive = True
                    if cell.aliveNeighbours < 2:
                        newGrid[r][c].alive = False
                    if cell.aliveNeighbours > 3:
                        newGrid[r][c].alive = False
                else:
                    if cell.aliveNeighbours == 3:
                        newGrid[r][c].alive = True
        
        self.grid = newGrid



        

if __name__ == "__main__":
    grid = GridWindow(pygame.display.set_mode((700, 600)), 50, 100, 600, 30)
    grid.grid_randomise()
    grid.conway_play()