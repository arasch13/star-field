"""Star field"""

# import modules from standard library
import sys
import pygame

# import custom modules
from settings import Settings
from star import Star, Starfield

GAME_TITLE = "Star field"


class GameClass:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.star_counter = 0
        self.settings = Settings()
        self._set_screen()
        self.starfield = Starfield(self)

    def start_game(self):
        while True:
            self.star_counter += self.clock.tick()
            if self.star_counter > self.settings.star_time:
                self.star_counter = 0
                star = Star(self)
                self.starfield.stars.append(star)
            self._check_events()
            self._update_physics()
            self._update_screen()

    # ----------------------------------------------  helper methods  --------------------------------------------------

    def _set_screen(self):
        """set initial screen properties"""
        # window size
        if self.settings.screen_mode == 'fullscreen':
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        elif self.settings.screen_mode == 'window':
            self.screen = pygame.display.set_mode(
                (self.settings.window_screen_width,
                 self.settings.window_screen_height)
            )
        # window title
        pygame.display.set_caption(GAME_TITLE)

    def _check_events(self):
        """listen to user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """key down events"""
        if event.key == getattr(pygame, self.settings.exit_game_button):
            sys.exit()

    def _update_physics(self):
        """calculate game physics"""
        self.starfield.move()

    def _update_screen(self):
        """update screen"""
        self.screen.fill(self.settings.bg_color)  # background color
        self.starfield.show()
        pygame.display.flip()  # only make recently drawn screen visible


# start game
if __name__ == '__main__':
    game = GameClass()
    game.start_game()
