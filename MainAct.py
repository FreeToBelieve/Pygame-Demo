import pygame
import random
import GameDeom.Explosion as Explosion
import GameDeom.EnemyAct as EnemyAct
font_name = 'Font/STXINWEI.TTF'
skill_before = list()
for i in range(0, 4):
    skill_before.append(pygame.transform.scale(pygame.image.load(f'Image/skill{i}_before.png'), (30, 30)))
skill_after = list()
for i in range(0, 4):
    skill_after.append(pygame.transform.scale(pygame.image.load(f'Image/skill{i}_after.png'), (30, 30)))
gold_file = 'Image/gold.png'


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surf, text_rect)


def draw_blood(surf, x, y, blood, blood_lenth=100, max_blood=100):
    if blood < 0:
        blood = 0
    blood_hight = 10
    fill = int((blood / max_blood) * blood_lenth)
    outline_rect = pygame.Rect(x, y, blood_lenth, blood_hight)
    fill_rect = pygame.Rect(x, y, fill, blood_hight)
    pygame.draw.rect(surf, (255, 0, 0), fill_rect)
    pygame.draw.rect(surf, (255, 255, 255), outline_rect, 1)


def draw_lives(surf, player, x, y, img):
    for i in range(0, player.lives):
        img_rect = img[player.type].get_rect()
        img_rect.x = x + i * 25
        img_rect.y = y
        surf.blit(img[player.type], img_rect)


def draw_skill(surf, player, x, y):
    img_rect = skill_before[player.type].get_rect()
    img_rect.x = x
    img_rect.y = y
    if not player.skill_cd:
        surf.blit(skill_before[player.type], img_rect)
    else:
        surf.blit(skill_after[player.type], img_rect)


def draw_gold(surf, x, y):
    gold = pygame.transform.scale(pygame.image.load(gold_file), (30, 30))
    img_rect = gold.get_rect()
    img_rect.x = x
    img_rect.y = y
    surf.blit(gold, img_rect)


# 玩家发出的动作击中敌人时
def hit_mobs(mobs, group, if_disappear, enemy_number, score, explosions, all_sprites, props, expl_sound, map_number, gold):
    bullet_hit_enemy = pygame.sprite.groupcollide(mobs, group, True, if_disappear)
    for hit in bullet_hit_enemy:
        enemy_number -= 1
        score += 100
        gold += random.randint(5, 10)
        exp1 = Explosion.Explosion(hit.rect.center, 'large')
        explosions.add(exp1)
        all_sprites.add(exp1)
        expl_sound.play()
        props_ran = random.randint(1, 10)  # 决定出现道具的随机数
        if props_ran == 2:
            prop = EnemyAct.creat_props(hit.rect.x, hit.rect.y)
            props.add(prop)
            all_sprites.add(prop)
        new_en_num = random.randint(0, 2)  # 将要新创建的敌机数量
        if enemy_number == 0 and new_en_num == 0:
            enemy_number += 1
            if map_number == 1:
                EnemyAct.new_enemy1(all_sprites, mobs)
            if map_number == 2:
                EnemyAct.new_enemy2(all_sprites, mobs)
        for i in range(0, new_en_num):
            enemy_number += 1
            if map_number == 1:
                EnemyAct.new_enemy1(all_sprites, mobs)
            if map_number == 2:
                EnemyAct.new_enemy2(all_sprites, mobs)
    return enemy_number, score, gold


def hit_boss(bosses, group, if_disappear, boss, damage, explosions, all_sprites, alter, score, gold):
    bullet_hit_boss = pygame.sprite.groupcollide(bosses, group, False, if_disappear)
    for hit in bullet_hit_boss:
        boss.blood -= damage
        exp2 = Explosion.Explosion(hit.rect.center, 'small')
        explosions.add(exp2)
        all_sprites.add(exp2)
        if boss.blood <= 0:
            boss.kill()
            gold += random.randint(1000, 2000)
            return 10, 0, gold
    return score, alter.count, gold
