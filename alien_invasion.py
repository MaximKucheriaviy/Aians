import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()
        

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.mainClock = pygame.time.Clock()
        self.loopTimer = 0
    def run_game(self):
        while True:
            self.loopTimer = self.mainClock.tick()
            self._check_ivents()
            self.ship.update()
            self._update_screen()
    def _check_ivents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.movingRight = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.movingRight = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ship.movingLeft = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.ship.movingLeft = False
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
