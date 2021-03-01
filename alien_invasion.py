import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

        """上色"""
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """开始游戏的主环"""
        while True:
            self._check_events()
            self._upsate_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _upsate_screen(self):
        """每次环时都会重绘屏幕"""
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        """让最近的绘制的屏幕可见"""
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
