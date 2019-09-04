import pygame
import pygame.sprite as sprite
WIDTH, HEIGHT = 600, 600


class Bullet(sprite.Sprite):
    def __init__(self, bullet, x, y, if_player, speedx=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy = -10
        self.if_player = if_player
        self.speedx = speedx

    def update(self, *args):
        if not self.if_player:
            self.speedy = 10
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.bottom > HEIGHT:
            self.kill()
