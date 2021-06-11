import colours
import pygame
vec = pygame.math.Vector2

# offsets = {
#     "up": (-1, 0),
#     "upRight": (-1, 1),
#     "right": (0, 1),
#     "downRight": (1, 1),
#     "down": (1, 0),
#     "downLeft": (-1, 1),
#     "left": (0, -1),
#     "upLeft": (-1, -1)
# }

class Cell():
    def __init__(self, background, i, j, gap, totalRows):
        self.row = i
        self.column = j
        self.x = j * gap
        self.y = i * gap
        self.width = gap
        self.alive = False
        self.colour = colours.DEAD_CELL
        self.totalRows = totalRows
        self.random = None

        self.background = background
        self.pos = vec(self.x, self.y)
        self.surface = pygame.Surface((self.width, self.width))
        self.rect = self.surface.get_rect(topleft=self.pos)
        
        self.neighbours = []
        self.aliveNeighbours = 0
        # self.checkingNeighbour = False
        
    # def check_neighbours(self):
    #     for cell in self.neighbours:
    #         if cell.alive:
    #             self.checkingNeighbour = True


    def is_alive(self):
        return self.alive


    def make_dead(self):
        self.colour = colours.DEAD_CELL


    def make_alive(self):
        self.colour = colours.ALIVE_CELL


    def get_neighbours(self, grid):
        neighbourList = [[-1, 0], [-1, 1], [0, 1], [1, 1], 
                         [1, 0], [1, -1], [0, -1], [-1, -1]]
        
        for neighbour in neighbourList:
            neighbour[0] += self.row
            neighbour[1] += self.column
        
        for neighbour in neighbourList:
            if neighbour[0] < 0:
                neighbour[0] += 30
            if neighbour[1] < 0:
                neighbour[1] += 30
            if neighbour[0] > 29:
                neighbour[0] -= 30
            if neighbour[1] > 29:
                neighbour[1] -= 30

        for neighbour in neighbourList:
            try:
                self.neighbours.append(grid[neighbour[0]][neighbour[1]])
            except:
                print(neighbour)

    def get_alive_neighbours(self):
        count = 0
        for neighbour in self.neighbours:
            if neighbour.is_alive():
                count += 1

        self.aliveNeighbours = count


    def draw(self):
        if self.alive:  # add self.checkingNeighour to check neighbours 
            self.make_alive()
            pygame.draw.rect(self.background, self.colour, self.rect)
        else:
            self.make_dead()
            pygame.draw.rect(self.background, self.colour, self.rect)
            
