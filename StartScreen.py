import pygame
import sys
import GameDeom.Button as Button
import GameDeom.SelectPlayer as SelectPlayer
import GameDeom.SelectCheckpoint as SelectCheckpoint
import GameDeom.Info as Info
background_filename = 'Image/strat_background.jpg'
gs_button_up = 'Image/strat_button_before.png'
gs_button_down = 'Image/strat_button_after.png'
gq_button_up = 'Image/return_button_before.png'
gq_button_down = 'Image/return_button_after.png'
select_button = 'Image/button_select.png'
info_button_up = 'Image/button_info_before.png'
info_button_down = 'Image/button_info_after.png'
player_status = list()
for i in range(0, 4):
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_left.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_right.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_invincible.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_left_invincible.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_right_invincible.png'), (100, 100)))
start_sound_file = 'Sound/StartGame.wav'


def start_screen(screen):
    game_start_button = Button.Button(gs_button_up, gs_button_down, (520, 200), 150, 70)
    game_quit_button = Button.Button(gq_button_up, gq_button_down, (520, 400), 150, 70)
    select_checkpoint_button = Button.Button(select_button, select_button, (80, 200), 150, 70)
    info_button = Button.Button(info_button_up, info_button_down, (80, 400), 150, 70)
    background = pygame.image.load(background_filename)
    background = pygame.transform.scale(background, (600, 600))
    clock = pygame.time.Clock()
    start_sound = pygame.mixer.Sound(start_sound_file)
    start_sound.play(loops=-1)
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        game_start_button.change(screen)
        game_quit_button.change(screen)
        select_checkpoint_button.change(screen)
        info_button.change(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if game_start_button.is_over():
                    start_sound.stop()
                    SelectPlayer.SelectPlayer(screen, player_status, 1)
                if game_quit_button.is_over():
                    sys.exit()
                if select_checkpoint_button.is_over():
                    start_sound.stop()
                    SelectCheckpoint.SelectCheckpoint(screen)
                if info_button.is_over():
                    start_sound.stop()
                    Info.Info(screen)
        pygame.display.flip()
