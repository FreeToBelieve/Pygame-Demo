import pygame
import pygame.sprite as sprite


class Other(sprite.Sprite):
    def __init__(self, other, x, y):
        sprite.Sprite.__init__(self)
        self.image = other
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = pygame.time.get_ticks()
        self.count = 0
