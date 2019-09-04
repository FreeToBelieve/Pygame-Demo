import pygame
import sys
import GameDeom.Button as Button
import GameDeom.MainAct as MainAct
import GameDeom.StartScreen as StarScreen
background_filename = 'Image/strat_background.jpg'
confirm_button_up = 'Image/confirm_button_before.png'
confirm_button_down = 'Image/confirm_button_after.png'
congratulation_sound_file = 'Sound/Congratulation.wav'


def Congratulation(screen):
    confirm_button = Button.Button(confirm_button_up, confirm_button_down, (250, 400), 120, 50)
    background = pygame.image.load(background_filename)
    background = pygame.transform.scale(background, (600, 600))
    clock = pygame.time.Clock()
    congratulation_sound = pygame.mixer.Sound(congratulation_sound_file)
    congratulation_sound.play(loops=-1)
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        MainAct.draw_text(screen, '恭喜！您已通关！')
        confirm_button.change(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if confirm_button.is_over():
                    StarScreen.start_screen(screen)
