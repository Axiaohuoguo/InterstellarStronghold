import pygame
from source import tools
from source import constants as CO


# 结束界面
class End_s:
    def __init__(self):
        self.backgroundimg = pygame.image.load(CO.BGPATH)
        self.start_01_img = pygame.image.load(CO.STPATH1)
        self.st_rect = self.start_01_img.get_rect()

    def update(self,surface):
        '''
        :param surface: 屏幕
        :return:
        '''
        # 加载背景图片\
        backgroundimg = tools.get_image(self.backgroundimg,0,0,CO.SCR_X,CO.SCR_Y,'NULL',1)
        surface.blit(backgroundimg,(0,0),backgroundimg.get_rect()) # 图像，绘制的位置，绘制的截面框
