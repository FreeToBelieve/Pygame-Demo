import pygame
import sys
import random
import GameDeom.EnemyAct as EnemyAct
import GameDeom.MainAct as MainAct
import GameDeom.Explosion as Explosion
import GameDeom.Boss as Boss
import GameDeom.Other as Other
import GameDeom.GameOver as GameOver
import GameDeom.Store as Store
WIDTH, HEIGHT = 600, 600


def Map2(screen, player, player_status, gold):
    FPS = 60
    SELF_BLOOD = player.max_blood
    player.blood = player.max_blood
    BOSS1_BLOOD = 3500
    clock = pygame.time.Clock()
    background_filename = 'Image/map2.jpg'
    background1 = pygame.transform.scale(pygame.image.load(background_filename), (WIDTH, HEIGHT))
    boss_file = pygame.image.load('Image/boss2.png').convert_alpha()
    alter_file = pygame.transform.scale(pygame.image.load('Image/alter.png').convert_alpha(), (300, 100))
    lives = list()
    bg_sound = pygame.mixer.Sound('Sound/map2.wav')
    bg_sound.play(loops=-1)
    expl_sound = pygame.mixer.Sound('Sound/explosion.wav')
    expl_sound.set_volume(0.4)
    props_sound = pygame.mixer.Sound('Sound/props.wav')
    props_sound.set_volume(0.4)
    for i in range(0, 4):
        lives.append(pygame.transform.scale(pygame.image.load(f'Image/live_num_{i}.png'), (20, 20)))
    enemy_number = 0  # 敌军总数
    score = 0  # 分数合计，达到一定分数出现Boos
    all_sprites = pygame.sprite.Group()  # 保存所有对象
    player_sprite = pygame.sprite.Group()  # 保存玩家对象
    player_lasers = pygame.sprite.Group() #玩家的激光对象
    mobs = pygame.sprite.Group()  # 小怪组保存所有小怪
    bullets = pygame.sprite.Group()  # 子弹组保存所有子弹
    enemy_bullets = pygame.sprite.Group()  # 敌人的子弹组
    explosions = pygame.sprite.Group()  # 所有的爆炸特效
    props = pygame.sprite.Group()  # 所有的道具对象
    bosses = pygame.sprite.Group()  # 所有的Boss对象
    lasers = pygame.sprite.Group()  # 所有敌人的激光技能对象
    skill = pygame.sprite.Group() # Boss的技能对象
    boss_mobs = pygame.sprite.Group() # Boss召唤的小怪对象
    boss = Boss.Boss(boss_file, BOSS1_BLOOD, 2)
    alter = Other.Other(alter_file, 100, 300)
    all_sprites.add(player)
    player_sprite.add(player)
    enemy_num = random.randint(6, 10)  # 敌人的数量
    for i in range(enemy_num):
        EnemyAct.new_enemy2(all_sprites, mobs)
        enemy_number += 1
    while True:
        clock.tick(FPS)
        screen.blit(background1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mobs.update(all_sprites, enemy_bullets)
        if player.lives <= 0:#判断玩家是否失败
            GameOver.GameOver(screen, 2, player, player_status, gold)
        num_score = MainAct.hit_mobs(mobs, bullets, True, enemy_number, score, explosions, all_sprites, props, expl_sound, 2, gold)#子弹击中敌人时
        enemy_number = num_score[0]
        score = num_score[1]
        gold = num_score[2]
        num_score = MainAct.hit_mobs(mobs, player_lasers, False, enemy_number, score, explosions, all_sprites, props, expl_sound, 2, gold)#激光击中敌人时
        enemy_number = num_score[0]
        score = num_score[1]
        bullet_hit_player = pygame.sprite.spritecollide(player, enemy_bullets, True, pygame.sprite.collide_circle)  # 玩家与子弹碰撞
        for hit in bullet_hit_player:
            if not player.if_invincible:
                player.blood -= 2
            exp2 = Explosion.Explosion(hit.rect.center, 'small')
            explosions.add(exp2)
            all_sprites.add(exp2)
            if player.lives <= 0:
                GameOver.GameOver(screen, 2, player, player_status, gold)
        laser_hit_player = pygame.sprite.spritecollide(player, lasers, False)  # 玩家与激光技能碰撞
        for hit in laser_hit_player:
            if not player.if_invincible:
                player.blood -= 1
            exp2 = Explosion.Explosion(hit.rect.center, 'small')
            explosions.add(exp2)
            all_sprites.add(exp2)
            if player.lives <= 0:
                GameOver.GameOver(screen, 2, player, player_status, gold)
        player_hits_enemy = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)  # 玩家与敌机碰撞时
        if player_hits_enemy:
            score += 100
            gold += random.randint(5, 10)
            if not player.if_invincible:
                player.blood -= 10
            exp1 = Explosion.Explosion(player.rect.center, 'large')
            explosions.add(exp1)
            all_sprites.add(exp1)
            expl_sound.play()
            EnemyAct.new_enemy2(all_sprites, mobs)
            if player.lives <= 0:
                GameOver.GameOver(screen, 2, player, player_status, gold)
        player_hit_skill = pygame.sprite.spritecollide(player, skill, True) # 玩家与Boss技能碰撞
        for hit in player_hit_skill:
            if not player.if_invincible:
                player.blood -= 10
            exp2 = Explosion.Explosion(hit.rect.center, 'small')
            explosions.add(exp2)
            all_sprites.add(exp2)
            expl_sound.play()
            if player.lives <= 0:
                GameOver.GameOver(screen, 2, player, player_status, gold)
        player_hit_boss = pygame.sprite.spritecollide(player, bosses, False, pygame.sprite.collide_circle)  # 玩家与Boss碰撞时
        if player_hit_boss:
            if not player.if_invincible:
                player.blood -= 20
            exp1 = Explosion.Explosion(player.rect.center, 'large')
            explosions.add(exp1)
            all_sprites.add(exp1)
            expl_sound.play()
            if player.lives <= 0:
                GameOver.GameOver(screen, 2, player, player_status, gold)
        player_hit_props = pygame.sprite.spritecollide(player, props, True)  # 玩家和道具碰撞
        for hit in player_hit_props:
            props_sound.play()
            if hit.type == 0:
                player.power_up()
            if hit.type == 1:
                if player.blood <= player.max_blood-20:
                    player.blood += 20
                else:
                    player.blood = SELF_BLOOD
            if hit.type == 2:
                player.invincible()
        bullet_hit_bullet = pygame.sprite.groupcollide(bullets, enemy_bullets, True, True)#子弹和子弹抵消
        score_count = MainAct.hit_boss(bosses, bullets, True, boss, player.attack, explosions, all_sprites, alter, score, gold)#子弹击中Boss
        score = score_count[0]
        alter.count = score_count[1]
        gold = score_count[2]
        score_count = MainAct.hit_boss(bosses, player_lasers, False, boss, 6, explosions, all_sprites, alter, score, gold)#激光击中Boss
        score = score_count[0]
        alter.count = score_count[1]
        gold = score_count[2]
        if score == 10 and alter.count == 0:
            player.lives = 3
            bg_sound.stop()
            Store.Store(screen, gold, player, player_status, 2)
        player_hit_bm = pygame.sprite.groupcollide(bullets, boss_mobs, True, True)#子弹击中Boss召唤的小怪
        for hit in player_hit_bm:
            exp1 = Explosion.Explosion(hit.rect.center, 'large')
            explosions.add(exp1)
            all_sprites.add(exp1)
        lasers_hit_bm = pygame.sprite.groupcollide(player_lasers, boss_mobs, False, True)#激光击中Boss召唤的小怪
        for hit in lasers_hit_bm:
            exp1 = Explosion.Explosion(hit.rect.center, 'large')
            explosions.add(exp1)
            all_sprites.add(exp1)
        # 出现Boos
        if score >= 20000:
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
                expl_sound.play()
            bosses.add(boss)
            all_sprites.add(boss)
        player_sprite.update(player_status, all_sprites, bullets, player_lasers)
        bullets.update()
        enemy_bullets.update()
        explosions.update()
        props.update()
        lasers.update()
        player_lasers.update()
        boss_mobs.update(all_sprites, enemy_bullets)
        skill.update()
        bosses.update(all_sprites, enemy_bullets, lasers, boss_mobs, skill)
        all_sprites.draw(screen)
        MainAct.draw_blood(screen, 5, 5, player.blood, player.max_blood, max_blood=SELF_BLOOD)
        MainAct.draw_lives(screen, player, 5, 25, lives)
        MainAct.draw_text(screen, '技能：', 16, 35, 50)
        MainAct.draw_skill(screen, player, 60, 50)
        MainAct.draw_gold(screen, 0, 100)
        MainAct.draw_text(screen, str(gold), 15, 70, 100)
        pygame.display.flip()
        pygame.display.update()
