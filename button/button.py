import pygame

class Button:
    def __init__(self, app, width = 100, height = 50, left = 10, top = 10, color = (180, 180, 180), fontPath = "./button/buttonFont.ttf", text = "Button", textColor = (0, 0, 0), hoverColor = (140, 140, 140), hoverEnable = False):
        if(not pygame.font.get_init()):
            pygame.font.init()
        self.screen = app.screen
        self.buttonRect = pygame.Rect(left, top, width, height)
        self.color = color
        self.font = pygame.font.Font(fontPath, 14)
        self.text = text
        self.textColor = textColor
        self.hoverColor = hoverColor
        self.hoverEnable = hoverEnable
        self.pressed = False

    def isHover(self):
        mousePosition = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePosition[0], mousePosition[1]):
            return True
        return False

    def isPressed(self, callback = False):
        if not self.isHover():
            return False
        if pygame.mouse.get_pressed()[0] and self.pressed:
            return False
        else:
            self.pressed = False
        if pygame.mouse.get_pressed()[0]:
            self.pressed = True
            if(callback):
                callback()
            return True
        return False


    def display(self):
        textSurface = self.font.render(self.text, True, self.textColor)
        textRect = textSurface.get_rect()
        textRect.center = self.buttonRect.center
        if self.hoverEnable:
            if self.isHover():
                pygame.draw.rect(self.screen, self.hoverColor, self.buttonRect)
            else:
                pygame.draw.rect(self.screen, self.color, self.buttonRect)
        else:
            pygame.draw.rect(self.screen, self.color, self.buttonRect)
        
        self.screen.blit(textSurface, textRect)

