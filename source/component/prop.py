from source import constants as CO
from source.tools import get_image
import pygame
import random
Sprite = pygame.sprite.Sprite

class Prop(Sprite):
    def __init__(self, pro_pos_x,pro_pos_y,pro_type):
        Sprite.__init__(self)
        self.pro_type = pro_type
        self.pro_pos_x = pro_pos_x
        self.pro_pos_y = pro_pos_y
        if pro_type == '1':
            self.image = pygame.image.load()
            self.health = 30  # 生命增加
        if pro_type == '2':
            self.image = pygame.image.load()
            self.hurt = 30  # 伤害增加

        if pro_type == '3':
            self.image = pygame.image.load()
            self.score = 1000  # 分数增加

        self.rect = self.image.get_rect()
        self.change = 0
        self.boom_change = 0
        self.rect.top = pro_pos_y  # 矩形左上角坐标
        self.rect.left = pro_pos_x  # 矩形左上角坐标
        self.temp = 0