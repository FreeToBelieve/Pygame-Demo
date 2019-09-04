import pygame
import random
import pygame.sprite as sprite
import GameDeom.Bullet as Bullet
bullet_surface = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Image/bullet2.png'), 180), (10, 40))
WIDTH, HEIGHT = 600, 600


class Enemy(sprite.Sprite):
    def __init__(self, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(enemy, (100, 100))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.5 / 2)
        # pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.rect.x = random.randrange(50, 551, 50)
        self.rect.y = random.randrange(-200, -50)
        self.speedy = 2
        self.speedx = random.randint(-5, 5)
        self.max_y = random.randrange(100, 201, 20)
        self.count = 0  #帧数移动计数，到10即改变方向并重新计数

    def update(self, all_sprites, enemy_bullets):
        #移动方式规则
        if self.rect.y < self.max_y:
            if self.count == 10:
                self.speedx = random.randint(-5, 5)
                self.count = 0
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            self.count += 1
        else:
            if self.count == 10:
                self.speedx = random.randint(-5, 5)
                self.count = 0
            self.rect.x += self.speedx
            self.count += 1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        #攻击形式规则
        ran = random.randint(0, 30)
        if ran == 1:
            self.shoot(all_sprites, enemy_bullets) #设置随机数，这样每一帧都有小概率发射子弹

    def shoot(self, all_sprites, enemy_bullets):
        bullet = Bullet.Bullet(bullet_surface, self.rect.x, self.rect.bottom, 0)
        all_sprites.add(bullet)
        enemy_bullets.add(bullet)
