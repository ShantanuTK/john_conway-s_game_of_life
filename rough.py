def conway_play(self):
    newGrid = copy.copy(self.grid)
    for row in self.grid:
        for cell in row:
            numberOfALiveNeighbours = len(self.get_neighbours(cell))

            if cell.is_alive():
                if numberOfALiveNeighbours == 3 or numberOfALiveNeighbours == 2:
                    newGrid[cell.row][cell.column].make_alive()
                if numberOfALiveNeighbours < 2:
                    newGrid[cell.row][cell.column].make_dead()
                if numberOfALiveNeighbours > 3:
                    newGrid[cell.row][cell.column].make_dead()
            else:
                if numberOfALiveNeighbours == 3:
                    newGrid[cell.row][cell.column].make_alive()

    self.grid = newGrid

def get_neighbours(self, cell):
        for direction in ["up", "upRight", "right", "downRight", "down", "downLeft", "left", "upLeft"]:
            xOffset = cell.x + (offsets[direction][0] * cell.width)
            yOffset = cell.y + (offsets[direction][1] * cell.width)

            if 0 <= xOffset < self.width and 0 <= yOffset < self.width:
                rowOffset = yOffset // cell.width
                columnOffset = xOffset // cell.width
                # with open("rough.txt", "a+") as file:
                #     file.write(str(rowOffset) + ", " + str(columnOffset) + "\n")
                neighbour = self.grid[rowOffset][columnOffset]

                if neighbour:
                    if neighbour.is_alive():
                        cell.neighbours.append(neighbour)

        return cell.neighbours
                

gridWindow = GridWindow(mainWindow, GRID_X, GRID_Y, GRID_WIDTH, GRID_ROWS)
importButton = Button(mainWindow, colours.BUTTON, 50, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, 'Import', gameFont)
randomButton = Button(mainWindow, colours.BUTTON, (WIDTH / 2 - BUTTON_WIDTH / 2), BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, 'Randomize', gameFont, gridWindow.grid_randomise)
resetButton = Button(mainWindow, colours.BUTTON, 500, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, 'Reset', gameFont, gridWindow.reset_grid)
    
if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos() #pos = (x, y)
            row, column = gridWindow.get_clicked_pos(pos)
            cell = gridWindow.grid[row][column]
            
            if cell.is_dead():
                cell.make_alive()

            if 50 <= pos[0] <= 50 + BUTTON_WIDTH  and 40 <= pos[1] <= 70:
                importButton.on_click()

            if (WIDTH / 2 - BUTTON_WIDTH / 2) <= pos[0] <= (WIDTH / 2 - BUTTON_WIDTH / 2) + BUTTON_WIDTH  and 40 <= pos[1] <= 70:
                randomButton.on_click()

            if 500 <= pos[0] <= 500 + BUTTON_WIDTH and 40 <= pos[1] <= 70:
                resetButton.on_click()

        elif pygame.mouse.get_pressed()[2]:
            pos = pygame.mouse.get_pos()
            row, column = gridWindow.get_clicked_pos(pos)

            cell = gridWindow.grid[row][column]
            if cell.is_alive():
                cell.make_dead()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gridWindow.conway_play()



for row in self.grid:
            for cell in row:
                cell.draw()

        self.draw_grid_lines()
        # self.surface.blit(self.image, self.rect)
        pygame.draw.rect(self.surface, colours.DEAD_CELL, self.rect)