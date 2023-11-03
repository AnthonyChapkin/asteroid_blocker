import pygame


class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 500
        self.y_pos = 400
        self.image = pygame.image.load('assets/graphics/planet.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (130, 130))
        self.rect = self.image.get_rect(center=(500, 400))
