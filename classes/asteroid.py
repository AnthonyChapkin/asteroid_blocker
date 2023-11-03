import pygame

import math
from random import randint, choice


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.speed = 5

        self.bounced_off = False

        self.x = randint(-200, 1200)
        if 0 <= self.x <= 1000:
            self.y = choice([randint(-200, -50), randint(850, 1000)])
        else:
            self.y = randint(-200, 1000)

        middle_x = 500
        middle_y = 400

        self.radians = math.atan2(self.y - middle_y, self.x - middle_x)
        self.distance = int(math.hypot(middle_x - self.x, middle_y - self.y) / self.speed)
        self.dist_x = math.cos(self.radians) * self.speed
        self.dist_y = math.sin(self.radians) * self.speed

        image_choice = choice(['asteroid_1', 'asteroid_2'])
        self.image = pygame.image.load(f'assets/graphics/asteroids/{image_choice}.png')
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def movement(self):
        self.x -= self.dist_x
        self.y -= self.dist_y
        self.rect.center = (self.x, self.y)

        if self.bounced_off and ((-10 > self.x or self.x > 1010) or (self.y < -10 or self.y > 810)):
            self.kill()

    def bounce_off(self):
        if not self.bounced_off:
            self.bounced_off = True
            self.dist_x = -self.dist_x
            self.dist_y = -self.dist_y

    def update(self):
        self.movement()
