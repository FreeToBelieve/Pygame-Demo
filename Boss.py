import pygame
import random
import pygame.sprite as sprite
import GameDeom.Bullet as Bullet
import GameDeom.Laser as Laser
import GameDeom.EnemyAct as EnemyAct
import GameDeom.Skill as Skill
bullet1_surface = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Image/bullet3.png'), 180), (10, 40))
bullet2_surface = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Image/bullet5.png'), 180), (10, 40))
bullet3_surface = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Image/bullet6.png'), 180), (40, 20))
bullet4_surface = pygame.transform.scale(pygame.transform.rotate(pygame.image.load('Image/bullet8.png'), 180), (40, 40))
skill_surface = pygame.transform.scale(pygame.image.load('Image/bullet7.png'), (30, 30))
laser_list = list()
for i in range(0, 6):
    filename = f'Image/laser{i}.png'
    laser_list.append(pygame.transform.scale(pygame.image.load(filename), (100, 500)))
laser1_list = list()
for i in range(0, 6):
    filename = f'Image/laser2_{i}.png'
    laser1_list.append(pygame.transform.scale(pygame.image.load(filename), (100, 500)))
shoot_sound_file = 'Sound/boss_shoot.wav'
WIDTH, HEIGHT = 600, 600


class Boss(sprite.Sprite):
    def __init__(self, boos, blood, type):
        sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(boos, (200, 200))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.5 / 2)
        #pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.rect.x = random.randint(200, 400)
        self.rect.y = -100
        self.speedx = random.randint(-2, 2)
        self.blood = blood
        self.type = type # 决定为第几关的Boss
        self.count = 0  # 帧数移动计数，到10即改变方向并重新计数

    def update(self, all_sprites, enemy_bullets, lasers, boss_mobs, skill):
        #移动方式规则
        if self.rect.y < 10:
            self.rect.y += 2
        self.rect.x += self.speedx
        self.count += 1
        if self.count >= 100:
            self.speedx = random.randint(-2, 2)
            self.count = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        #攻击方式规则
        shoot_sound = pygame.mixer.Sound(shoot_sound_file)
        if self.type == 1:
            attack_ran = random.randint(0, 20)#普攻释放平均数
            if attack_ran == 1:
                self.shoot1(all_sprites, enemy_bullets)
                shoot_sound.play()
            skill_ran = random.randint(0, 360)#技能释放随机数
            if skill_ran == 60:
                laser = Laser.Laser(laser_list, self.rect.centerx, self.rect.centery)
                all_sprites.add(laser)
                lasers.add(laser)
        if self.type == 2:
            attack_ran = random.randint(0, 60)
            if attack_ran == 1:
                self.shoot2(all_sprites, enemy_bullets)
                shoot_sound.play()
            skill1_ran = random.randint(0, 120)
            if skill1_ran == 60:
                EnemyAct.new_enemy2(all_sprites, boss_mobs)
            skill2_ran = random.randint(0, 60)
            if skill2_ran == 1:
                self.skill1(all_sprites, skill)
        if self.type == 3:
            attack_ran = random.randint(0, 60)
            if attack_ran == 2:
                self.shoot3(all_sprites, enemy_bullets)
                shoot_sound.play()
            skill1_ran = random.randint(0, 40)
            if skill1_ran == 30:
                skill0 = Skill.Skill(skill_surface, self.rect.centerx, self.rect.centery)
                all_sprites.add(skill0)
                skill.add(skill0)
            skill2_ran = random.randint(0, 20)
            if skill2_ran == 10:
                self.skill1(all_sprites, skill)
            skill3_ran = random.randint(0, 360)
            if skill3_ran == 60:
                laser = Laser.Laser(laser1_list, self.rect.centerx, self.rect.centery)
                all_sprites.add(laser)
                lasers.add(laser)

    def shoot1(self, all_sprites, enemy_bullets):
        bullet = list()
        bullet.append(Bullet.Bullet(bullet1_surface, self.rect.centerx-60, self.rect.bottom, 0, -2))
        bullet.append(Bullet.Bullet(bullet1_surface, self.rect.centerx-30, self.rect.bottom, 0, -2))
        bullet.append(Bullet.Bullet(bullet1_surface, self.rect.centerx, self.rect.bottom, 0))
        bullet.append(Bullet.Bullet(bullet1_surface, self.rect.centerx+30, self.rect.bottom, 0, 2))
        bullet.append(Bullet.Bullet(bullet1_surface, self.rect.centerx+60, self.rect.bottom, 0, 2))
        for i in bullet:
            all_sprites.add(i)
            enemy_bullets.add(i)

    def shoot2(self, all_sprites, enemy_bullets):
        bullet = list()
        for i in range(1, 6):
            bullet.append(Bullet.Bullet(bullet2_surface, self.rect.centerx - i * 20, self.rect.bottom, 0, -1))
        bullet.append(Bullet.Bullet(bullet2_surface, self.rect.centerx, self.rect.bottom, 0))
        for i in range(1, 6):
            bullet.append(Bullet.Bullet(bullet2_surface, self.rect.centerx + i * 20, self.rect.bottom, 0, 1))
        all_sprites.add(bullet)
        enemy_bullets.add(bullet)

    def shoot3(self, all_sprites, enemy_bullets):
        bullet = list()
        for i in range(0, 5):
            bullet.append(Bullet.Bullet(bullet4_surface, self.rect.centerx - i * 40, self.rect.bottom - i * 20, 0))
        for i in range(1, 5):
            bullet.append(Bullet.Bullet(bullet4_surface, self.rect.centerx + i * 40, self.rect.bottom - i * 20, 0))
        all_sprites.add(bullet)
        enemy_bullets.add(bullet)

    def skill1(self, all_sprites, skill):
        bullet = Bullet.Bullet(bullet3_surface, self.rect.centerx, self.rect.bottom, 0, random.randint(-2, 2))
        all_sprites.add(bullet)
        skill.add(bullet)
