import pygame
vec = pygame.math.Vector2
import colours

class Button():
    def __init__(self, background, colour, x, y, width, height, text, gameFont, function=None):
        self.background = background
        self.pos = vec(x, y)
        self.width = width
        self.height = height
        self.text = text
        self.colour = colour
        self.font = gameFont
        self.surface = pygame.Surface((self.width, self.height))
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.pos
        self.function = function


    def update(self):
        self.rect.topleft = self.pos


    def draw(self):
        self.surface.fill(self.colour)
        textLabel = self.font.render(self.text, True, colours.TEXT)
        textRect = textLabel.get_rect(center=(self.width / 2, self.height / 2))
        self.surface.blit(textLabel, textRect)
        self.background.blit(self.surface, self.rect)

    def mouse_hovering(self, pos):
        if pos[0] > self.pos[0] and pos[0] < self.pos[0] + self.width:
            if pos[1] > self.pos[1] and pos[1] < self.pos[1] + self.height:
                return True

        return False

    def on_click(self):
        if self.function:
            self.function()