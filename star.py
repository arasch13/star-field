import random
import pygame
import math


class Star:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.x = random.randint(
            self.screen_rect.center[0] - self.screen_rect.width / 10,
            self.screen_rect.center[0] + self.screen_rect.width / 10
        )
        self.y = random.randint(
            self.screen_rect.center[1] - self.screen_rect.height / 10,
            self.screen_rect.center[1] + self.screen_rect.height / 10
        )
        self.initial_x = self.x
        self.initial_y = self.y
        self.tail_length = self.settings.star_tail_length
        self.color = self.settings.star_color
        self.radius = self.settings.star_radius

    def show(self):
        x_ratio_to_center, y_ratio_to_center = self.center_distance()
        radius = self.radius * max(abs(x_ratio_to_center), abs(y_ratio_to_center))
        tail_length = self.tail_length * self.settings.star_speed / 5 + radius * 3
        pygame.draw.circle(self.screen, self.color, (round(self.x), round(self.y)), round(radius))

        tail_x = self.initial_x
        tail_y = self.initial_y
        initial_vector_length = math.sqrt((tail_x - self.x) ** 2 + (tail_y - self.y) ** 2)
        if initial_vector_length > tail_length:
            tail_x = self.x - tail_length * (self.x - self.initial_x) / initial_vector_length
            tail_y = self.y - tail_length * (self.y - self.initial_y) / initial_vector_length
        pygame.draw.line(self.screen, self.color, (round(tail_x), round(tail_y)),
                         (round(self.x), round(self.y)), round(self.radius / 2))

    def move(self):
        x_ratio_to_center, y_ratio_to_center = self.center_distance()
        # self.tail_x = self.x
        # self.tail_y = self.y
        self.x = self.x + x_ratio_to_center * self.settings.star_speed
        self.y = self.y + y_ratio_to_center * self.settings.star_speed

    def center_distance(self):
        x_ratio_to_center = (self.x - self.screen_rect.center[0]) / (self.screen_rect.width / 2) * 5
        y_ratio_to_center = (self.y - self.screen_rect.center[1]) / (self.screen_rect.height / 2) * 5
        return x_ratio_to_center, y_ratio_to_center


class Starfield:
    def __init__(self, ai_game):
        self.stars = []
        self.screen_rect = ai_game.screen.get_rect()
        # for _ in range(ai_game.settings.star_nr):
        #     star = Star(ai_game)
        #     self.stars.append(star)

    def show(self):
        for star in self.stars:
            star.show()

    def move(self):
        for star in self.stars:
            star.move()
            if star.x < 0 or star.x > self.screen_rect.width or star.y < 0 or star.y > self.screen_rect.height:
                self.stars.remove(star)
