import pygame


class Chip:
    def __init__(self, app, number = 0):
        if not pygame.font.get_init():
            pygame.font.init()
        self.number = number
        self.settings = app.settings
        self.screen = app.screen
        self.image = pygame.image.load("./assets/button.png")
        self.rect = self.image.get_rect()
        rectSize = (self.settings.gameFieldSize) / 4 * 0.9
        self.rect.width = rectSize
        self.rect.height = rectSize
        self.image = pygame.transform.scale(self.image, (rectSize, rectSize))
        self.font = pygame.font.Font("./fonts/ALBA.ttf" , 40)
        self.canMove = False
    def isHover(self):
        mousePoss = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePoss[0], mousePoss[1]):
            return True
        return 
    def isPressed(self):
        if not self.isHover():
            return False
        if pygame.mouse.get_pressed()[0] and self.canMove:
            return True
        return False
    def display(self, rect):
        self.rect.center = rect.center
        self.screen.blit(self.image, self.rect)
        textSurface = self.font.render(str(self.number), True, (0, 0, 0))
        textRect = textSurface.get_rect()
        textRect.center = self.rect.center
        self.screen.blit(textSurface, textRect)
