import pygame
import random
import pygame.sprite as sprite
WIDTH, HEIGHT = 600, 600


class Skill(sprite.Sprite):
    def __init__(self, skill, x, y):
        sprite.Sprite.__init__(self)
        self.image = skill
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(-5, 5)
        self.count = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.count += 1
        if self.count == 100:
            self.speedx = random.randint(-5, 5)
            self.speedy = random.randint(-5, 5)
            self.count = 0
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right > WIDTH or self.rect.left < 0:
            self.kill()
