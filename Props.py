import pygame
import random
import pygame.sprite as sprite
WIDTH, HEIGHT = 600, 600


class Props(sprite.Sprite):
    def __init__(self, props, x, y, type):
        sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(props, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = random.randint(-1, 1)
        self.speedy = random.randint(-1, 1)
        self.count = 0
        self.type = type #道具类型：0为子弹增强，1为恢复，2为护盾

    def update(self, *args):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.count += 1
        if self.count == 100:
            self.speedx = random.randint(-1, 1)
            self.speedy = random.randint(-1, 1)
            self.count = 0
        if self.rect.bottom < 0 or self.rect.top > HEIGHT or self.rect.right > WIDTH or self.rect.left < 0:
            self.kill()
