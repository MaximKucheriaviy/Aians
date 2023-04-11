import pygame
from chip.chip import Chip
import random

class GameField:
    def __init__(self, app):
        random.seed()
        self.sound = pygame.mixer.Sound('./sounds/slide.mp3')
        self.screen = app.screen
        self.settings = app.settings
        self.fields = []
        self.randomMoves = 100
        self.randomiseTriger = False
        for i in range(0, 4):
            self.fields.append([])
            for j in range(0, 4):
                borderSize = self.settings.gameFieldSize / 4
                left = self.settings.gameFieldLeft + (borderSize * j)
                top = self.settings.gameFieldTop + (borderSize * i)
                chip = None
                if i != 3 or j != 3:
                    chip = Chip(app,  j + 1 + i * 4)
                obj = {'field': pygame.rect.Rect(left, top, borderSize, borderSize), 'chip': chip}
                self.fields[i].append(obj)
    def setMowebleChips(self):
        for item in self.fields:
            for field in item:
                if field['chip'] is None:
                    continue
                field['chip'].canMove = False
        for i in range(0, 4):
            for j in range(0, 4):
                if self.fields[i][j]['chip'] is None:
                    if i + 1 < 4:
                        self.setCanMove(i + 1, j, i, j)
                    if i - 1 >= 0:
                        self.setCanMove(i - 1, j, i, j)
                    if j + 1 < 4:
                        self.setCanMove(i, j + 1, i, j)
                    if j - 1 >= 0:
                        self.setCanMove(i, j - 1, i, j)
    def setCanMove(self, chipI, chipJ, targetI, tagetJ):
        self.fields[chipI][chipJ]['chip'].canMove = (targetI, tagetJ)
        
    def chipClickPrecess(self):
        for item in self.fields:
            moved = False
            for field in item:
                if(field['chip'] is None):
                    continue
                if(field['chip'].isPressed()):
                    self.moveFieldSmoth(field['chip'])
                    field['chip'] = None
                    self.sound.play()
                    moved = True
                    break
            if moved:
                break
    def randomise(self):
        if not self.randomiseTriger:
            return        
        while True:
            i = random.randint(0, 3)
            j = random.randint(0, 3)
            if self.fields[i][j]['chip'] is None:
                continue
            if not self.fields[i][j]['chip'].canMove:
                continue
            self.moveField(self.fields[i][j]['chip'])
            self.fields[i][j]['chip'] = None
            self.randomMoves -= 1
            if self.randomMoves == 0:
                self.randomiseTriger = False
            break
    def moveField(self, chip):
        self.fields[chip.canMove[0]][chip.canMove[1]]['chip'] = chip
    def moveFieldSmoth(self, chip):
        self.fields[chip.canMove[0]][chip.canMove[1]]['chip'] = chip
        self.fields[chip.canMove[0]][chip.canMove[1]]['chip'].moving = True
    def display(self):
        for item in self.fields:
            for rect in item:
                pygame.draw.rect(self.screen, pygame.Color(0, 255, 0), rect['field'])
        for item in self.fields:
            for field in item:
                if(field['chip'] is None):
                    continue
                field['chip'].display(field['field'])
                
