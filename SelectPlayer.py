import pygame
import sys
import GameDeom.Button as Button
import GameDeom.MainAct as MainAct
import GameDeom.Player as Player
import GameDeom.Map1 as Map1
import GameDeom.Map2 as Map2
import GameDeom.Map3 as Map3
background_filename = 'Image/strat_background.jpg'
select_button_up = ('Image/plane0.png', 'Image/plane1.png', 'Image/plane2.png', 'Image/plane3.png')
select_button_down = ('Image/plane0_after.png', 'Image/plane1_after.png', 'Image/plane2_after.png', 'Image/plane3_after.png')
select_button = list()#存放确定按钮类
select_sound_file = 'Sound/SelectPlayer.wav'


def SelectPlayer(screen, player_status, select_number):
    background = pygame.transform.scale(pygame.image.load(background_filename), (600, 600))
    clock = pygame.time.Clock()
    select_sound = pygame.mixer.Sound(select_sound_file)
    select_sound.play(loops=-1)
    gold = 0#重置金钱数
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        MainAct.draw_text(screen, "请选择要使用的角色", 30, 150, 100)
        MainAct.draw_text(screen, "ATK : 40    DEF : 100", 15, 150, 150)
        MainAct.draw_text(screen, "技能:弹幕之雨", 15, 150, 170)
        MainAct.draw_text(screen, "向前方锥形范围发射19枚导弹", 15, 160, 190)
        MainAct.draw_text(screen, "ATK : 55    DEF : 70", 15, 150, 230)
        MainAct.draw_text(screen, "技能:激光", 15, 150, 250)
        MainAct.draw_text(screen, "向正前方发射威力巨大的激光", 15, 160, 270)
        MainAct.draw_text(screen, "ATK : 35    DEF : 120", 15, 150, 310)
        MainAct.draw_text(screen, "技能:神圣庇佑", 15, 150, 330)
        MainAct.draw_text(screen, "3秒钟内获得无敌", 15, 160, 350)
        MainAct.draw_text(screen, "ATK : 50    DEF : 80", 15, 150, 390)
        MainAct.draw_text(screen, "技能:上帝之手", 15, 150, 410)
        MainAct.draw_text(screen, "恢复20生命值", 15, 150, 430)
        for i in range(0, 4):
            select_button.append(Button.Button(select_button_up[i], select_button_down[i], (400, 160+90*i), 70, 70))
            select_button[i].change(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if select_button[0].is_over():
                    status = player_status[0:6]
                    player = Player.Player(status, 0, 40, 100)
                    select_sound.stop()
                    select_check(screen, player, status, select_number, gold)
                if select_button[1].is_over():
                    status = player_status[6:12]
                    player = Player.Player(status, 1, 55, 70)
                    select_sound.stop()
                    select_check(screen, player, status, select_number, gold)
                if select_button[2].is_over():
                    status = player_status[12:18]
                    player = Player.Player(status, 2, 35, 120)
                    select_sound.stop()
                    select_check(screen, player, status, select_number, gold)
                if select_button[3].is_over():
                    status = player_status[18:24]
                    player = Player.Player(status, 3, 50, 80)
                    select_sound.stop()
                    select_check(screen, player, status, select_number, gold)
        pygame.display.flip()


def select_check(screen, player, status, select_number, gold):
    if select_number == 1:
        Map1.Map1(screen, player, status, gold)
    if select_number == 2:
        Map2.Map2(screen, player, status, gold)
    if select_number == 3:
        Map3.Map3(screen, player, status, gold)
