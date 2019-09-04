import pygame
import random
import GameDeom.Enemy as Enemy
import GameDeom.Props as Props
props_create = list()
props_create.append(pygame.image.load('Image/props1.png'))
props_create.append(pygame.image.load('Image/props2.png'))
props_create.append(pygame.image.load('Image/props3.png'))


def new_enemy1(all_sprites, mobs):
    ran = random.randint(1, 4)
    enemy = pygame.image.load(f'Image/enemy{ran}.png').convert_alpha()
    m = Enemy.Enemy(enemy)
    all_sprites.add(m)
    mobs.add(m)


def new_enemy2(all_sprites, mobs):
    ran = random.randint(2, 7)
    enemy = pygame.image.load(f'Image/enemy{ran}.png').convert_alpha()
    m = Enemy.Enemy(enemy)
    all_sprites.add(m)
    mobs.add(m)


def creat_props(x, y):
    props_ran = random.randint(0, 9)
    if props_ran == 0:
        props = Props.Props(props_create[0], x, y, 0)
    elif 1 <= props_ran <= 7:
        props = Props.Props(props_create[1], x, y, 1)
    else:
        props = Props.Props(props_create[2], x, y, 2)
    return props
