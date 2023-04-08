import pygame
from chip.chip import Chip

class GameField:
    def __init__(self, app):
        self.screen = app.screen
        self.settings = app.settings
        self.fields = []
        for i in range(0, 4):
            self.fields.append([])
            for j in range(0, 4):
                borderSize = self.settings.gameFieldSize / 4
                left = self.settings.gameFieldLeft + (borderSize * j)
                top = self.settings.gameFieldTop + (borderSize * i)
                chip = None
                if i != 3 or j != 3:
                    chip = Chip(app, j + 1 + i * 4)
                obj = {'field': pygame.rect.Rect(left, top, borderSize, borderSize), 'chip': chip}
                self.fields[i].append(obj)

    def display(self):
        for item in self.fields:
            for rect in item:
                pygame.draw.rect(self.screen, pygame.Color(0, 255, 0), rect['field'])
        for item in self.fields:
            for field in item:
                if(field['chip'] is None):
                    continue
                field['chip'].display(field['field'])
                
