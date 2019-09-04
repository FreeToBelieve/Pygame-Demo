import pygame
import pygame.sprite as sprite
laser_sound_file = 'Sound/laser.wav'


class Laser(sprite.Sprite):
    def __init__(self, laser, x, y):
        sprite.Sprite.__init__(self)
        self.image_list = laser
        self.image = self.image_list[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        self.frame = 0

    def update(self, *args):
        now = pygame.time.get_ticks()
        laser_sound = pygame.mixer.Sound(laser_sound_file)
        laser_sound.play()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.image_list):
                self.kill()
        else:
            x = self.rect.x
            y = self.rect.y
            self.image = self.image_list[self.frame]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
