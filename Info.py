import pygame
import sys
import GameDeom.Button as Button
import GameDeom.MainAct as MainAct
import GameDeom.StartScreen as StarScreen
background_filename = 'Image/strat_background.jpg'
confirm_button_up = 'Image/confirm_button_before.png'
confirm_button_down = 'Image/confirm_button_after.png'
return_button_up = 'Image/return_button_before.png'
return_button_down = 'Image/return_button_after.png'
info_sound_file = 'Sound/Info.wav'


def Info(screen):
    confirm_button = Button.Button(confirm_button_up, confirm_button_down, (200, 500), 120, 50)
    return_button = Button.Button(return_button_up, return_button_down, (400, 500), 120, 50)
    background = pygame.image.load(background_filename)
    background = pygame.transform.scale(background, (600, 600))
    clock = pygame.time.Clock()
    info_sound = pygame.mixer.Sound(info_sound_file)
    info_sound.play(loops=-1)
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        confirm_button.change(screen)
        return_button.change(screen)
        MainAct.draw_text(screen, '操作方法：', 30, 150, 50)
        MainAct.draw_text(screen, 'W  向上移动', 30, 150, 100)
        MainAct.draw_text(screen, 'S  向下移动', 30, 150, 200)
        MainAct.draw_text(screen, 'A  向左移动', 30, 150, 300)
        MainAct.draw_text(screen, 'D  向右移动', 30, 150, 400)
        MainAct.draw_text(screen, 'J 射击', 30, 400, 100)
        MainAct.draw_text(screen, 'K 技能', 30, 400, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if confirm_button.is_over():
                    info_sound.stop()
                    StarScreen.start_screen(screen)
                if return_button.is_over():
                    info_sound.stop()
                    StarScreen.start_screen(screen)
        pygame.display.flip()
