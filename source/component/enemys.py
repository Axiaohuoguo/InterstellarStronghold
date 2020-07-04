# 敌人
from source import constants as CO
from source.tools import get_image
import pygame

Sprite = pygame.sprite.Sprite


class Enemys(Sprite):

    def __init__(self, en1_pos_x,en1_pos_y,en_type):
        Sprite.__init__(self)
        if en_type == '1':
            self.image = pygame.image.load(CO.EN1_01_IMGPATH)
            self.health = 20
        self.rect = self.image.get_rect()
        self.change = 0
        self.boom_change = 0
        self.rect.topleft = (en1_pos_x,en1_pos_y)  # 矩形左上角坐标
        self.speed = 20
        self.temp = 0

    def move_l(self):
        self.rect.right += self.speed

    def move_r(self):
        self.rect.right -= self.speed

    def change_en1(self):  # 控制角色动画
        if self.change == 0:
            self.image = pygame.image.load(CO.EN1_01_IMGPATH)
            self.change = 1

        elif self.change == 1:
            self.image = pygame.image.load(CO.EN1_02_IMGPATH)
            self.change = 2

        elif self.change == 2:
            self.image = pygame.image.load(CO.EN1_03_IMGPATH)
            self.change = 3

        elif self.change == 3:
            self.image = pygame.image.load(CO.EN1_04_IMGPATH)
            self.change = 0

    def get_en_pos(self):
        pos = self.rect.topleft
        return pos


class Bomb(Sprite):
    # 初始化爆炸
    def __init__(self):
        Sprite.__init__(self)
        # 加载爆炸资源

        self.image = [pygame.image.load(CO.EN1_BOOM_PATH + '/boom0' + str(v) + ".png") for v in range(1, 3)]
        # 设置当前爆炸播放索引
        self.index = 0
        # 图片爆炸播放间隔
        self.interval = 10
        self.interval_index = 0
        # 爆炸位置
        self.position = [0, 0]
        # 是否可见
        self.visible = False

    # 设置爆炸播放的位置
    def set_pos(self, pos):
        self.position[0] = pos[0]
        self.position[1] = pos[1]

    def en_boom_l(self):
        self.position[0] = self.position[0] + 20

    def en_boom_r(self):
        self.position[0] = self.position[0] - 20

    # 爆炸播放
    def action(self):
        # 如果爆炸对象状态不可见，则不计算坐标
        if not self.visible:
            return
        # 控制每一帧图片的播放间隔
        self.interval_index += 1
        if self.interval_index < self.interval:
            return
        self.interval_index = 0

        self.index = self.index + 1
        if self.index >= len(self.image):
            self.index = 0
            self.visible = False

    # 绘制爆炸
    def draw(self,Scene):
        # 如果对象不可见，则不绘制
        if not self.visible:
            return
        Scene.blit(self.image[self.index], (self.position[0], self.position[1]))


