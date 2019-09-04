import pygame
import GameDeom.StartScreen as StartScreen
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Deom')
size = WIDTH, HEIGHT = 600, 600
FPS = 60
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
while True:
    StartScreen.start_screen(screen)
