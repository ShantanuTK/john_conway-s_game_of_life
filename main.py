"""
RULES:
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

"""

from grid_window_class import *
import colours
import pygame
import sys
from buttons import Button

WIDTH = 700
HEIGHT = 700
FPS = 60
GRID_X = 50
GRID_Y = 100
GRID_WIDTH = 600
GRID_HEIGHT = 400
GRID_ROWS = 30
BUTTON_Y = 40
BUTTON_HEIGHT = 30
BUTTON_WIDTH = 150

run = True

pygame.init()

mainWindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
gameFont = pygame.font.Font("freesansbold.ttf", 20)
state = "setting"

def play_game():
    global state
    state = "play"

def pause_game():
    global state
    state = "pause"

def reset_grid():
    global state
    state = "setting"
    gridWindow.reset_grid()

def cursor_on_grid(pos):
    if pos[0] > GRID_X and pos[0] < WIDTH - GRID_X:
        if pos[1] > GRID_Y and pos[1] < WIDTH:
            return True
    
    return False

gridWindow = GridWindow(mainWindow, GRID_X, GRID_Y, GRID_WIDTH, GRID_ROWS)
playButton = Button(mainWindow, colours.BUTTON, 50, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, 'Play', gameFont, play_game)
pauseButton = Button(mainWindow, colours.BUTTON, (WIDTH / 2 - BUTTON_WIDTH / 2), BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, 'Pause', gameFont, pause_game)
resetButton = Button(mainWindow, colours.BUTTON, 500, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, 'Reset', gameFont, reset_grid)

#-------------------------------------------------- SETTING FUNCTIONS ----------------------------------------------------#
def settings_get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # Activate one cell condition
        # if pygame.mouse.get_pressed()[0]:   # Activate multiple cell condition
            pos = pygame.mouse.get_pos()
            if cursor_on_grid(pos):
                gridWindow.click_cell(pos)
            else:
                if playButton.mouse_hovering(pos):
                    playButton.on_click()
                if pauseButton.mouse_hovering(pos):
                    pauseButton.on_click()
                if resetButton.mouse_hovering(pos):
                    resetButton.on_click()

def settings_draw():
    mainWindow.fill(colours.BACKGROUND)
    gridWindow.draw()
    playButton.draw()
    pauseButton.draw()
    resetButton.draw()

def settings_update():
    # gridWindow.update()
    pygame.display.update()

#-------------------------------------------------- PAUSE FUNCTIONS ----------------------------------------------------#

def pause_get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # Activate one cell condition
        # if pygame.mouse.get_pressed()[0]:   # Activate multiple cell condition
            pos = pygame.mouse.get_pos()
            if cursor_on_grid(pos):
                gridWindow.click_cell(pos)
            else:
                if playButton.mouse_hovering(pos):
                    playButton.on_click()
                if pauseButton.mouse_hovering(pos):
                    pauseButton.on_click()
                if resetButton.mouse_hovering(pos):
                    resetButton.on_click()

def pause_draw():
    mainWindow.fill(colours.BACKGROUND)
    gridWindow.draw()
    playButton.draw()
    pauseButton.draw()
    resetButton.draw()

def pause_update():
    # gridWindow.update()
    pygame.display.update()


#-------------------------------------------------- PLAY FUNCTIONS ----------------------------------------------------#

def play_get_events():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:  # Activate one cell condition
        # if pygame.mouse.get_pressed()[0]:   # Activate multiple cell condition
            pos = pygame.mouse.get_pos()
            if cursor_on_grid(pos):
                gridWindow.click_cell(pos)
            else:
                if playButton.mouse_hovering(pos):
                    playButton.on_click()
                if pauseButton.mouse_hovering(pos):
                    pauseButton.on_click()
                if resetButton.mouse_hovering(pos):
                    resetButton.on_click()

def play_draw():
    mainWindow.fill(colours.BACKGROUND)
    gridWindow.draw()
    playButton.draw()
    pauseButton.draw()
    resetButton.draw()

def play_update():
    # gridWindow.update()
    gridWindow.conway()
    pygame.display.update()

#-------------------------------------------------- GAME LOOP ----------------------------------------------------#

while run:
    if state == "setting":
        settings_get_events()
        settings_draw()
        settings_update()
    if state == "play":
        play_get_events()
        play_draw()
        play_update()
    if state == "pause":
        pause_get_events()
        pause_draw()
        pause_update()

    # print(state)
    clock.tick(FPS // 6)
