import pygame
import sys
import GameDeom.MainAct as MainAct
import GameDeom.Button as Button
import GameDeom.SelectPlayer as SelectPlayer
background_filename = 'Image/select.jpg'
player_status = list()
for i in range(0, 4):
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_left.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_right.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_invincible.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_left_invincible.png'), (100, 100)))
    player_status.append(pygame.transform.scale(pygame.image.load(f'Image/player{i}_right_invincible.png'), (100, 100)))
confirm_button_up = 'Image/confirm_button_before.png'
confirm_button_down = 'Image/confirm_button_after.png'
select_sound_file = 'Sound/SelectCheckpoint.wav'


def SelectCheckpoint(screen):
    background = pygame.transform.scale(pygame.image.load(background_filename), (600, 600))
    clock = pygame.time.Clock()
    select_sound = pygame.mixer.Sound(select_sound_file)
    select_sound.play(loops=-1)
    confirm_list = list()
    for i in range(0, 3):
        confirm_list.append(Button.Button(confirm_button_up, confirm_button_down, (200, 150 * (i + 1)), 120, 50))
    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))
        MainAct.draw_text(screen, '第一关', 50, 350, 150)
        MainAct.draw_text(screen, '第二关', 50, 350, 300)
        MainAct.draw_text(screen, '第三关', 50, 350, 450)
        for i in range(0, 3):
            confirm_list[i].change(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if confirm_list[0].is_over():
                    select_sound.stop()
                    SelectPlayer.SelectPlayer(screen, player_status, 1)
                if confirm_list[1].is_over():
                    select_sound.stop()
                    SelectPlayer.SelectPlayer(screen, player_status, 2)
                if confirm_list[2].is_over():
                    select_sound.stop()
                    SelectPlayer.SelectPlayer(screen, player_status, 3)
        pygame.display.flip()
