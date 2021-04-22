"""Settings"""


class Settings:

    def __init__(self):
        """Settings"""
        # screen settings
        self.screen_mode = 'window'  # 'window' or 'fullscreen'
        self.window_screen_width = 1000
        self.window_screen_height = 800
        self.bg_color = (0, 0, 0)
        # control settings
        self.exit_game_button = 'K_ESCAPE'
        # game settings
        self.star_color = (255, 255, 255)
        self.star_radius = 1.6
        self.star_time = 30  # ms
        self.star_speed = 0.3
        self.star_tail_length = 20
