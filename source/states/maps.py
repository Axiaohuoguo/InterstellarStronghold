# 地图控制
from source import constants as CO
from source.tools import get_image
import pygame


class MapCon:
    def __init__(self):
        self.lv0_backgroundimg = pygame.image.load(CO.LV1_MAPPATH)  # lv0 地图图片
        self.lv0_rect = self.lv0_backgroundimg.get_rect()  # lv0 地图rect
        self.lv0_rect_x = self.lv0_rect[2] # 图片w
        self.lv0_rect_y = self.lv0_rect[3] # 图片h
        self.lv_x_speed = -100 # 地图初始位置
        self.lv_y_speed = 0
        self.map_check()

    def map_loade(self,surface):
        '''
        :param surface: 屏幕
        :param key_f: 前进
        :param key_q: 后腿
        :return:
        '''
        # 加载地图图片
        backgroundimg = get_image(self.lv0_backgroundimg,0,0,self.lv0_rect_x,self.lv0_rect_y,'NULL',2)
        # self.lv_x = self.lv_x+30
        surface.blit(backgroundimg,(0,0),(self.lv_x_speed, self.lv_y_speed, self.lv0_rect_x, CO.SCR_Y)) # 图像，绘制的位置，绘制的截面框


    # def map_update(self,key):
    #
    #     if key == 'A':
    #         self.lv_x_speed = self.lv_x_speed - 30
    #     elif key == 'D':
    #         self.lv_x_speed = self.lv_x_speed + 30

    def map_update_r(self): # 右

        self.lv_x_speed = self.lv_x_speed - 40

    def map_update_l(self): # 左
        self.lv_x_speed = self.lv_x_speed + 40

    def map_check(self): # 检测地图是否越界
        if self.lv_x_speed < 0:
            self.lv_x_speed = 0
        elif self.lv_x_speed >= 1920*4:
            self.lv_x_speed = 1920*4

    def get_lv_x_speed(self):
        return self.lv_x_speed


