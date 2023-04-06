import pygame
from chip.chip import Chip

class GameField:
    def __init__(self, app):
        self.screen = app.screen
        self.settings = app.settings
        self.fields = []
        self.chips = []
        for i in range(0, 4):
            self.fields.append([])
            self.chips.append([])
            for j in range(0, 4):
                borderSize = self.settings.gameFieldSize / 4
                left = self.settings.gameFieldLeft + (borderSize * j)
                top = self.settings.gameFieldTop + (borderSize * i)
                self.fields[i].append(pygame.rect.Rect(left, top, borderSize, borderSize))
                self.chips[i].append(Chip(app))

    def display(self):
        for item in self.fields:
            for rect in item:
                pygame.draw.rect(self.screen, pygame.Color(0, 255, 0), rect)
        for i in range(0, 4):
            for j in range(0, 4):
                self.chips[i][j].display(self.fields[i][j])
