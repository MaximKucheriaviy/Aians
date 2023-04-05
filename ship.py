import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.game = ai_game

        self.image = pygame.image.load('assets/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.movingRight = False
        self.movingLeft = False

        self.x = float(self.rect.x)
        

    def update(self):
        if self.movingRight:
            self.x += self.settings.ship_speed * self.game.loopTimer / 5
        if self.movingLeft:
            self.x -= self.settings.ship_speed * self.game.loopTimer / 5
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)