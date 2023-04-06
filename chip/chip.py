import pygame

class Chip:
    def __init__(self, app, number = 0, ):
        self.number = number
        self.settings = app.settings
        self.screen = app.screen
        self.image = pygame.image.load("./assets/button.png")
        self.rect = self.image.get_rect()
        rectSize = (self.settings.gameFieldSize) / 4 * 0.9
        self.rect.width = rectSize
        self.rect.height = rectSize
        self.image = pygame.transform.scale(self.image, (rectSize, rectSize))
    def display(self, rect):
        self.rect.center = rect.center
        self.screen.blit(self.image, self.rect)
