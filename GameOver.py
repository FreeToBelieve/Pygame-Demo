import pygame
import sys
import GameDeom.Button as Button
import GameDeom.MainAct as MainAct
import GameDeom.Map1 as Map1
import GameDeom.Map2 as Map2
import GameDeom.Map3 as Map3
import GameDeom.StartScreen as StartScreen
background_filename = 'Image/strat_background.jpg'
restart_button_up = 'Image/button_restart_up.png'
restart_button_down = 'Image/button_restart_down.png'
menu_button_up = 'Image/button_menu_up.png'
menu_button_down = 'Image/button_menu_down.png'


def GameOver(screen, number_of_map, player, player_status, gold):
    background = pygame.transform.scale(pygame.image.load(background_filename), (600, 600))
    restart_button = Button.Button(restart_button_up, restart_button_down, (150, 400), 100, 50)
    menu_button = Button.Button(menu_button_up, menu_button_down, (350, 400), 100, 50)
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        MainAct.draw_text(screen, 'Game Over!', 50, 200, 200)
        restart_button.change(screen)
        menu_button.change(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if restart_button.is_over():
                    if number_of_map == 1:
                        player.lives = 3
                        pygame.mixer.stop()
                        Map1.Map1(screen, player, player_status, gold)
                    if number_of_map == 2:
                        player.lives = 3
                        pygame.mixer.stop()
                        Map2.Map2(screen, player, player_status, gold)
                    if number_of_map == 3:
                        player.lives = 3
                        pygame.mixer.stop()
                        Map3.Map3(screen, player, player_status, gold)
                if menu_button.is_over():
                    pygame.mixer.stop()
                    StartScreen.start_screen(screen)
        pygame.display.flip()
