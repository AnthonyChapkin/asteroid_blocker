import pygame

import math


class Moon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 243
        self.y_pos = 138
        self.image = pygame.image.load('assets/graphics/moon.png').convert_alpha()
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def player_input(self):
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        self.x_pos = 500 + 150*((mouse_pos_x - 500) / (math.sqrt((mouse_pos_x - 500)**2 + (mouse_pos_y - 400)**2)))
        self.y_pos = 400 + 150*((mouse_pos_y - 400) / (math.sqrt((mouse_pos_x - 500)**2 + (mouse_pos_y - 400)**2)))

    def update(self):
        self.player_input()
        self.rect.center = (self.x_pos, self.y_pos)

