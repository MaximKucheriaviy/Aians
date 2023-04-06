import sys
import pygame
from settings import Settings
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.mainClock = pygame.time.Clock()
        self.loopTimer = 0

        self.button = Button(self, fontPath="./fonts/buttonFont.ttf", hoverEnable=True)
        self.button2 = Button(self, fontPath="./fonts/buttonFont.ttf", top=70, color=(0, 255, 0), hoverEnable=True)

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            self.loopTimer = self.mainClock.tick()
            self._check_ivents()
            self._update_screen()
    def _check_ivents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if self.button.isPressed():
            print("Button pressed")
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.button.display()
        self.button2.display()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
