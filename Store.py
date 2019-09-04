import pygame
import sys
import GameDeom.MainAct as MainAct
import GameDeom.Button as Button
import GameDeom.Map2 as Map2
import GameDeom.Map3 as Map3
next_button_file = 'Image/button_next.png'
background_filename = 'Image/strat_background.jpg'
store_sound_file = 'Sound/Store.wav'
atk_up = 'Image/store_ATK_before.png'
atk_down = 'Image/store_ATK_after.png'
def_up = 'Image/store_DEF_before.png'
def_down = 'Image/store_DEF_after.png'


def Store(screen, gold, player, player_status, check_num):
    background = pygame.transform.scale(pygame.image.load(background_filename), (600, 600))
    clock = pygame.time.Clock()
    store_sound = pygame.mixer.Sound(store_sound_file)
    store_sound.play(loops=-1)
    next_button = Button.Button(next_button_file, next_button_file, (250, 500), 120, 50)
    atk_button = Button.Button(atk_up, atk_down, (200, 300), 80, 80)
    def_button = Button.Button(def_up, def_down, (400, 300), 80, 80)
    last_time_suc = pygame.time.get_ticks()
    last_time_fail = pygame.time.get_ticks()
    suc_alter = False#购买成功提示
    fail_alter = False#购买失败提示
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        next_button.change(screen)
        atk_button.change(screen)
        def_button.change(screen)
        MainAct.draw_text(screen, '商店', 30, 150, 100)
        MainAct.draw_text(screen, '升级武器：ATK+5', 20, 200, 200)
        MainAct.draw_text(screen, '升级血量：DEF+20', 20, 400, 200)
        MainAct.draw_text(screen, '$2000', 20, 200, 400)
        MainAct.draw_text(screen, '$2000', 20, 400, 400)
        MainAct.draw_gold(screen, 450, 100)
        MainAct.draw_text(screen, str(gold), 20, 500, 100)
        now = pygame.time.get_ticks()
        if suc_alter:
            MainAct.draw_text(screen, '购买成功！', 20, 200, 450)
        if fail_alter:
            MainAct.draw_text(screen, '购买失败！', 20, 300, 450)
        if now - last_time_suc > 2000:
            suc_alter = False
        if now - last_time_fail > 2000:
            fail_alter = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if atk_button.is_over():
                    if gold >= 2000:
                        gold -= 2000
                        player.attack += 5
                        suc_alter = True
                        last_time_suc = pygame.time.get_ticks()
                    else:
                        fail_alter = True
                        last_time_fail = pygame.time.get_ticks()
                if def_button.is_over():
                    if gold >= 2000:
                        gold -= 2000
                        player.max_blood += 20
                        suc_alter = True
                        last_time_suc = pygame.time.get_ticks()
                    else:
                        fail_alter = True
                        last_time_fail = pygame.time.get_ticks()
                if next_button.is_over():
                    if check_num == 1:
                        store_sound.stop()
                        Map2.Map2(screen, player, player_status, gold)
                    if check_num == 2:
                        store_sound.stop()
                        Map3.Map3(screen, player, player_status, gold)
            pygame.display.flip()
