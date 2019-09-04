import pygame
import pygame.sprite as sprite
from collections import defaultdict
explosion_dic = defaultdict(list)
for i in range(1, 5):
    filename = f'Image/explosion{i}.png'
    explosion = pygame.transform.scale(pygame.image.load(filename), (70, 70))
    explosion_dic['large'].append(explosion)
for i in range(1, 7):
    filename = f'Image/explosion_small_{i}.png'
    explosion = pygame.transform.scale(pygame.image.load(filename), (30, 30))
    explosion_dic['small'].append(explosion)


class Explosion(sprite.Sprite):
    def __init__(self, center, size):
        sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_dic[size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self, *args):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_dic[self.size]):
                self.kill()
        else:
            center = self.rect.center
            self.image = explosion_dic[self.size][self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = center
