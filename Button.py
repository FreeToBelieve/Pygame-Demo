import pygame
button_sound_file = 'Sound/button.wav'


#Button类定义了游戏中的所有的按钮
class Button(object):

    def __init__(self, up_image, down_image, position, width, height):
        self.up_image = pygame.transform.scale(pygame.image.load(up_image).convert_alpha(), (width, height))
        self.down_image = pygame.transform.scale(pygame.image.load(down_image).convert_alpha(), (width, height))
        self.position = position
        self.is_play = False

    #判断鼠标是否在按钮上
    def is_over(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x, y = self.position
        width, height = self.up_image.get_size()
        in_x = x - width / 2 < mouse_x < x + width / 2
        in_y = y - height / 2 < mouse_y < y + height / 2
        return in_x and in_y

    #按下按钮时改变按钮的样式
    def change(self, screen):
        x, y = self.position
        width, height = self.up_image.get_size()
        if self.is_over():
            screen.blit(self.down_image, (x - width / 2, y - height / 2))
            if not self.is_play:
                button_sound = pygame.mixer.Sound(button_sound_file)
                button_sound.play()
                self.is_play = True
        else:
            self.is_play = False
            screen.blit(self.up_image, (x - width / 2, y - height / 2))


if __name__ == '__main__':
    gs_button_up = 'C:\\Apps\\常用素材\\电话.png'
    gs_button_down = 'C:\\Apps\\常用素材\\邮箱.png'
    pygame.init()
    screen = pygame.display.set_mode((300, 200), 0, 32)
    button = Button(gs_button_up, gs_button_down, (150, 100), 120, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((200, 200, 200))
        button.change(screen)
        pygame.display.update()
