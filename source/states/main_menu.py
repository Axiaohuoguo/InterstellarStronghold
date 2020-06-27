import pygame
from source import tools
from source import constants as CO


# 主菜单控制
class MainMenu:
    def __init__(self):
        self.backgroundimg = pygame.image.load(CO.BGPATH)
        self.start_01_img = pygame.image.load(CO.STPATH1)
        self.start_02_img = pygame.image.load(CO.STPATH2)
        self.st_rect = self.start_01_img.get_rect()
        self.st_rect_x = 0
        self.st_rect_y = 0

    def update(self,surface,pos):
        '''
        :param surface: 屏幕
        :param pos: 鼠标位置
        :return:
        '''
        # print(backgroundimg.get_rect())
        # 加载背景图片\

        backgroundimg = tools.get_image(self.backgroundimg,0,0,CO.SCR_X,CO.SCR_Y,'NULL',1)
        surface.blit(backgroundimg,(0,0),backgroundimg.get_rect()) # 图像，绘制的位置，绘制的截面框

        mouse_x =pos[0]
        mouse_y =pos[1]
        print("==",pos)
        # 554 * 94
        # (CO.SCR_Y//2 + 94//2  <= mouse_x <= (CO.SCR_Y//2 + 800))
        if (mouse_x >= CO.SCR_X //2 - 554//2 and mouse_x <= CO.SCR_X//2 +554//2 ) and\
                (mouse_y >= CO.SCR_Y//2 and mouse_y<= CO.SCR_Y //2 + 94):  # 判断鼠标是否在开始按钮之上
            stimg = pygame.image.load(CO.STPATH1)
            stimg = tools.get_image(stimg, 0, 0, stimg.get_rect()[2], stimg.get_rect()[3], CO.COLOR_LU, 1) #
            surface.blit(stimg, (CO.SCR_X//2-554//2, CO.SCR_Y//2), stimg.get_rect())
        else:
            stimg = pygame.image.load(CO.STPATH2)
            stimg = tools.get_image(stimg, 0, 0, stimg.get_rect()[2], stimg.get_rect()[3], CO.COLOR_LU, 1)
            print("st -", stimg.get_rect())
            surface.blit(stimg, (CO.SCR_X//2-554//2, CO.SCR_Y//2), stimg.get_rect())

