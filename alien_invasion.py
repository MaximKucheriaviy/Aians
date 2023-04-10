import sys
import pygame
from settings import Settings
from button.button import Button
from gameField.gameField import GameField

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.bg_color
        self.mainClock = pygame.time.Clock()
        self.loopTimer = 0

        self.button = Button(self, hoverEnable=True)
        self.button2 = Button(self, top=70, color=(0, 255, 0), hoverEnable=True)

        self.gameField = GameField(self)

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            self.loopTimer = self.mainClock.tick()
            self._check_ivents()
            self.process()
            self._update_screen()
    def _check_ivents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if self.button.isPressed():
            print("Button pressed")
    def process(self):
        self.gameField.setMowebleChips()
        self.gameField.chipClickPrecess()
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.button.display()
        self.button2.display()
        self.gameField.display()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
