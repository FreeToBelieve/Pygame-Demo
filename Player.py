import pygame
import random
import pygame.sprite as sprite
import GameDeom.Bullet as Bullet
import GameDeom.Laser as Laser
laser_list = list()
for i in range(0, 6):
    filename = f'Image/laser1_{i}.png'
    laser_list.append(pygame.transform.scale(pygame.image.load(filename), (100, 500)))
bullet_surface = pygame.transform.scale(pygame.image.load('Image/bullet1.png'), (10, 40))
bullet_skill0 = pygame.transform.scale(pygame.image.load('Image/bullet4.png'), (20, 60))
shoot_sound_file = 'Sound/shoot.wav'
skill_sound_file = 'Sound/player_skill.wav'
WIDTH, HEIGHT = 600, 600


class Player(sprite.Sprite):
    def __init__(self, player, type, attack, blood):
        pygame.sprite.Sprite.__init__(self)
        self.image = player[0]
        self.blood = blood
        self.max_blood = blood
        self.attack = attack
        self.skill_cd = False
        self.skill_last = pygame.time.get_ticks()
        self.rect = self.image.get_rect()
        self.radius = 25
        # pygame.draw.circle(self.image, (255, 0, 0), self.rect.center, self.radius)
        self.rect.centerx = 400
        self.rect.bottom = 580
        self.speedx = 0
        self.speedy = 0
        self.status = 0
        self._power = 0
        self.type = type#决定是哪一个角色
        self.lives = 3#玩家生命数
        self.if_invincible = False#标记是否无敌
        self.invincible_time = pygame.time.get_ticks()#无敌时间
        self.shoot_delay = 250
        self.last_shoot = pygame.time.get_ticks()

    def update(self, player, all_sprites, bullets, player_lasers):
        self.speedx = 0
        self.speedy = 0
        self.image = player[self.status]
        keystate = pygame.key.get_pressed()
        #无敌判定
        if self.if_invincible and pygame.time.get_ticks() - self.invincible_time > 3000:
            self.if_invincible = False
        #移动控制规则
        if keystate[pygame.K_a]:
            if self.if_invincible:
                self.status = 4
            else:
                self.status = 1
            self.speedx = -8
        else:
            if self.if_invincible:
                self.status = 3
            else:
                self.status = 0
            if keystate[pygame.K_d]:
                if self.if_invincible:
                    self.status = 5
                else:
                    self.status = 2
                self.speedx = 8
        if keystate[pygame.K_w]:
            self.speedy = -3
        if keystate[pygame.K_s]:
            self.speedy = 3
        if keystate[pygame.K_j]:
            self.shoot(all_sprites, bullets)
            shoot_sound = pygame.mixer.Sound(shoot_sound_file)
            shoot_sound.set_volume(0.4)
            shoot_sound.play()

        #判断技能是否CD
        now = pygame.time.get_ticks()
        if now-self.skill_last >= 20000:
            self.skill_cd = False
        # 各个机型所带的技能
        if not self.skill_cd:
            if keystate[pygame.K_k]:
                self.skill_cd = True
                self.skill_last = pygame.time.get_ticks()
                if self.type == 0:
                    self.skill(all_sprites, bullets)
                    skill_sound = pygame.mixer.Sound(skill_sound_file)
                    skill_sound.play()
                if self.type == 1:
                    laser = Laser.Laser(laser_list, self.rect.centerx, self.rect.top-500)
                    all_sprites.add(laser)
                    player_lasers.add(laser)
                if self.type == 2:
                    self.invincible()
                if self.type == 3:
                    if self.blood < self.max_blood - 20:
                        self.blood += 20
                    else:
                        self.blood = self.max_blood
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        #血量为0时执行的动作
        if self.blood <= 0:
            self.lives -= 1
            self.blood = self.max_blood
            self.rect.centerx = 400
            self.rect.bottom = 580
            self.invincible()

    def skill(self, all_sprites, bullets):
        skill = list()
        for i in range(1, 10):
            skill.append(Bullet.Bullet(bullet_skill0, self.rect.centerx - i * 20, self.rect.top, 1, -1))
        skill.append(Bullet.Bullet(bullet_skill0, self.rect.centerx, self.rect.top, 1))
        for i in range(1, 10):
            skill.append(Bullet.Bullet(bullet_skill0, self.rect.centerx + i * 20, self.rect.top, 1, 1))
        all_sprites.add(skill)
        bullets.add(skill)

    def shoot(self, all_sprites, bullets):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            self.last_shoot = now
            bullet = list()
            if self._power == 0:
                bullet.append(Bullet.Bullet(bullet_surface, self.rect.centerx, self.rect.top, 1))
            for i in range(1, self._power+1):
                bullet.append(Bullet.Bullet(bullet_surface, self.rect.centerx-(i*10), self.rect.top, 1))
                bullet.append(Bullet.Bullet(bullet_surface, self.rect.centerx+(i*10), self.rect.top, 1))
            all_sprites.add(bullet)
            bullets.add(bullet)

    def invincible(self):
        self.if_invincible = True
        self.invincible_time = pygame.time.get_ticks()
        self.status = 3


    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, power):
        if power > 3:
            self._power = 3
        self._power = power

    def power_up(self):
        if self._power < 3:
            self._power += 1
