# 敌人
from source import constants as CO
from source.tools import get_image
import pygame

Sprite = pygame.sprite.Sprite


class Enemys(Sprite):

    def __init__(self, en1_pos_x,en1_pos_y):
        Sprite.__init__(self)
        self.enemy1_img = pygame.image.load(CO.EN1_01_IMGPATH)
        self.en1_rect = self.enemy1_img.get_rect()
        self.change = 0
        self.en1_rect.topleft = (en1_pos_x,en1_pos_y)  # 矩形左上角坐标
        self.en_01_speed_x = 0
        self.en_01_speed_y = 0
        self.speed = 20

    def move_l(self):
        self.en1_rect.right += self.speed

    def move_r(self):
        self.en1_rect.right -= self.speed

    def change_en1(self): # 控制角色动画

        if self.change == 0:
            self.enemy1_img = pygame.image.load(CO.EN1_01_IMGPATH)
            self.change = 1

        elif self.change == 1:
            self.enemy1_img = pygame.image.load(CO.EN1_02_IMGPATH)
            self.change = 2

        elif self.change == 2:
            self.enemy1_img = pygame.image.load(CO.EN1_03_IMGPATH)
            self.change = 3

        elif self.change == 3:
            self.enemy1_img = pygame.image.load(CO.EN1_04_IMGPATH)
            self.change = 0
