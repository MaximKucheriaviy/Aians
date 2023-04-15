import sys
import pygame
from settings import Settings
from button.button import Button
from gameField.gameField import GameField

class ChipsGame:
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.bg_color

        self.button = Button(self, left= 420, top=20, color=(163, 128, 82), hoverEnable=True, text="Roll")

        self.gameField = GameField(self)

        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            self._check_ivents()
            self.process()
            self._update_screen()
    def _check_ivents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if self.button.isPressed():
            self.gameField.randomiseTriger = True
            self.gameField.randomMoves = 100
    def process(self):
        self.gameField.setMowebleChips()
        self.gameField.chipClickPrecess()
        self.gameField.randomise()
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.button.display()
        self.gameField.display()
        pygame.display.flip()


if __name__ == '__main__':
    game = ChipsGame()
    game.run_game()
