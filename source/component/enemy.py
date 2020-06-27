# 敌人
from source import constants as CO
from source.tools import get_image
import pygame
Sprite = pygame.sprite.Sprite


class Enemy:

    def __init__(self):

        self.enemy1_img = pygame.image.load(CO.EN1_01_IMGPATH)
        self.en1_rect = self.enemy1_img.get_rect()

        self.p1_rect_x = self.en1_rect[2]
        self.p1_rect_y = self.en1_rect[3]

        self.speed_x = 3000 # CO.SCR_X // 2   # 初始x移动速度 ，位置
        self.speed_y =  CO.SCR_Y//2  # 初始y移动速度 ，位置
        self.change = 0

    def enemy_load(self, Surface):
        # 加载敌人图图片
        enemy_img = get_image(self.enemy1_img,0,0,self.p1_rect_x,self.p1_rect_y,CO.COLOR_LU,1)
        # self.lv_x = self.lv_x+30
        Surface.blit(enemy_img,(self.speed_x,self.speed_y),self.en1_rect) # 图像，绘制的位置，绘制的截面框

    def en1_uodate_r(self):  # 角色右移动
        self.speed_x = self.speed_x + 40

    def en1_uodate_l(self):  # 角色左移
        self.speed_x = self.speed_x - 40

    def change_en1(self):  # 控制角色动画
        if self.change == 0 :
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
