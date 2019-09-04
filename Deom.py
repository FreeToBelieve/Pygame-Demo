import pygame
import sys
import random
import GameDeom.StartScreen as StartScreen
import GameDeom.Player as Player
import GameDeom.Enemy as Enemy
import GameDeom.EnemyAct as EnemyAct
import GameDeom.MainAct as MainAct
import GameDeom.Explosion as Explosion
import GameDeom.Boss as Boss
import GameDeom.Other as Other
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Deom')
size = WIDTH, HEIGHT = 600, 600
FPS = 60
SELF_BLOOD = 100
BOSS1_BLOOD = 2000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background_filename = 'Image/map1.jpg'
# start_screen_sound = 'C:\\Apps\\python 学习\\neusoft_study\\GameDeom\\Sound\\bgm_startscreen.wav'
player_status = list()
player_status.append(pygame.transform.scale(pygame.image.load('Image/player.png').convert_alpha(), (100, 100)))
player_status.append(pygame.transform.scale(pygame.image.load('Image/player_left.png').convert_alpha(), (100, 100)))
player_status.append(pygame.transform.scale(pygame.image.load('Image/player_right.png').convert_alpha(), (100, 100)))
player_status.append(pygame.transform.scale(pygame.image.load('Image/player_invincible.png').convert_alpha(), (100, 100)))
player_status.append(pygame.transform.scale(pygame.image.load('Image/player_left_invincible.png').convert_alpha(), (100, 100)))
player_status.append(pygame.transform.scale(pygame.image.load('Image/player_right_invincible.png').convert_alpha(), (100, 100)))
background1 = pygame.transform.scale(pygame.image.load(background_filename), (WIDTH, HEIGHT))
boss_file = pygame.image.load('Image/boss1.png').convert_alpha()
alter_file = pygame.transform.scale(pygame.image.load('Image/alter.png').convert_alpha(), (300, 100))
lives = pygame.transform.scale(pygame.image.load('Image/live_num.png'), (20, 20))
enemy_number = 0 #敌军总数
score = 0 #分数合计，达到一定分数出现Boos
# start_sound = pygame.mixer.Sound(start_screen_sound)
# start_sound.play()
all_sprites = pygame.sprite.Group() #保存所有对象
player_sprite = pygame.sprite.Group() #保存玩家对象
mobs = pygame.sprite.Group() #小怪组保存所有小怪
bullets = pygame.sprite.Group() #子弹组保存所有子弹
enemy_bullets = pygame.sprite.Group() #敌人的子弹组
explosions = pygame.sprite.Group() #所有的爆炸特效
backgrounds = pygame.sprite.Group() #所有的背景图
props = pygame.sprite.Group() #所有的道具对象
bosses = pygame.sprite.Group() #所有的Boss对象
lasers = pygame.sprite.Group() #所有激光技能对象
others = pygame.sprite.Group() #所有其它对象
player = Player.Player(player_status)
boss = Boss.Boss(boss_file, BOSS1_BLOOD)
alter = Other.Other(alter_file, 100, 300)
all_sprites.add(player)
player_sprite.add(player)
enemy_num = random.randint(4, 7) #敌人的数量
for i in range(enemy_num):
    EnemyAct.new_enemy(all_sprites, mobs)
    enemy_number += 1
while StartScreen.start_screen(screen):
    pygame.display.update()
while True:
    clock.tick(FPS)
    screen.blit(background1, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mobs.update(all_sprites, enemy_bullets)
    bullet_hit_enemy = pygame.sprite.groupcollide(mobs, bullets, True, True)#子弹击中敌人
    for hit in bullet_hit_enemy:
        enemy_number -= 1
        score += 100
        exp1 = Explosion.Explosion(hit.rect.center, 'large')
        explosions.add(exp1)
        all_sprites.add(exp1)
        props_ran = random.randint(1, 10)#决定出现道具的随机数
        if props_ran == 2:
            prop = EnemyAct.creat_props(hit.rect.x, hit.rect.y)
            props.add(prop)
            all_sprites.add(prop)
        new_en_num = random.randint(0, 2)#将要新创建的敌机数量
        if enemy_number == 0 and new_en_num == 0:
            enemy_number += 1
            EnemyAct.new_enemy(all_sprites, mobs)
        for i in range(0, new_en_num):
            enemy_number += 1
            EnemyAct.new_enemy(all_sprites, mobs)
    bullet_hit_player = pygame.sprite.spritecollide(player, enemy_bullets, True, pygame.sprite.collide_circle)#玩家与子弹碰撞
    for hit in bullet_hit_player:
        if not player.if_invincible:
            player.blood -= 2
        exp2 = Explosion.Explosion(hit.rect.center, 'small')
        explosions.add(exp2)
        all_sprites.add(exp2)
        if player.lives <= 0:
            sys.exit()
    laser_hit_player = pygame.sprite.spritecollide(player, lasers, False)#玩家与激光技能碰撞
    for hit in laser_hit_player:
        if not player.if_invincible:
            player.blood -= 1
        exp2 = Explosion.Explosion(hit.rect.center, 'small')
        explosions.add(exp2)
        all_sprites.add(exp2)
        if player.lives <= 0:
            sys.exit()
    player_hits_enemy = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)#玩家与敌机碰撞时
    if player_hits_enemy:
        score += 100
        if not player.if_invincible:
            player.blood -= 10
        exp1 = Explosion.Explosion(player.rect.center, 'large')
        explosions.add(exp1)
        all_sprites.add(exp1)
        EnemyAct.new_enemy(all_sprites, mobs)
    player_hit_boss = pygame.sprite.spritecollide(player, bosses, False, pygame.sprite.collide_circle)#玩家与Boss碰撞时
    if player_hit_boss:
        if not player.if_invincible:
            player.blood -= 50
        if player.lives <= 0:
            sys.exit()
    player_hit_props = pygame.sprite.spritecollide(player, props, True)#玩家和道具碰撞
    for hit in player_hit_props:
        if hit.type == 0:
            player.power_up()
        if hit.type == 1:
            if player.blood <= 80:
                player.blood += 20
            else:
                player.blood = SELF_BLOOD
        if hit.type == 2:
            player.invincible()
    bullet_hit_bullet = pygame.sprite.groupcollide(bullets, enemy_bullets, True, True)
    bullet_hit_boss = pygame.sprite.groupcollide(bosses, bullets, False, True)
    for hit in bullet_hit_boss:
        boss.blood -= 40
        exp2 = Explosion.Explosion(hit.rect.center, 'small')
        explosions.add(exp2)
        all_sprites.add(exp2)
        if boss.blood <= 0:
            boss.kill()
            score = 0
            alter.count = 0
    #出现Boos
    if score >= 1000:
        all_sprites.add(alter)
        if alter.count >= 60:
            all_sprites.remove(alter)
        else:
            alter.count += 1
        if boss.alive():
            MainAct.draw_blood(screen, 200, 5, boss.blood, 200, BOSS1_BLOOD)
        for mob in mobs:
            mob.kill()
            exp1 = Explosion.Explosion(mob.rect.center, 'large')
            explosions.add(exp1)
            all_sprites.add(exp1)
        bosses.add(boss)
        all_sprites.add(boss)
    player_sprite.update(player_status, all_sprites, bullets)
    bullets.update()
    enemy_bullets.update()
    explosions.update()
    props.update()
    lasers.update()
    bosses.update(all_sprites, enemy_bullets, lasers)
    all_sprites.draw(screen)
    MainAct.draw_blood(screen, 5, 5, player.blood, max_blood=SELF_BLOOD)
    MainAct.draw_lives(screen, player.lives, 5, 25, lives)
    pygame.display.flip()
    pygame.display.update()
