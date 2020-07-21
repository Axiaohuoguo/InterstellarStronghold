# 敌人
from source import constants as CO
from source.tools import get_image
import pygame
import random
Sprite = pygame.sprite.Sprite


class Enemys(Sprite):

    def __init__(self, en1_pos_x,en1_pos_y,en_type):
        Sprite.__init__(self)
        self.en_type = en_type
        self.en1_pos_x = en1_pos_x
        self.en1_pos_y = en1_pos_y
        if en_type == '1':
            self.image = pygame.image.load(CO.EN1_01_IMGPATH)
            self.health = 20
            self.bullet_img = CO.EN_BULLET_01
            self.en_bullets = pygame.sprite.Group()
            self.en_bullet_img = pygame.image.load(CO.EN_BULLET_01)

        if en_type == '2':
            self.image = pygame.image.load(CO.EN2_01_IMGPATH)
            self.health = 20
            self.bullet_img = CO.EN_BULLET_01
            self.en_bullets = pygame.sprite.Group()
            self.en_bullet_img = pygame.image.load(CO.EN_BULLET_01)

        if en_type == '3':
            self.image = pygame.image.load(CO.EN_BOOS1_IMGPATH)
            self.health = 500
            self.bullet_img = CO.EN_BULLET_01
            self.en_bullets = pygame.sprite.Group()
            self.en_bullet_img = pygame.image.load(CO.EN_BULLET_01)

        self.rect = self.image.get_rect()
        self.change = 0
        self.boom_change = 0
        self.rect.top = en1_pos_y  # 矩形左上角坐标
        self.rect.left = en1_pos_x  # 矩形左上角坐标
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
            self.change = 4

        elif self.change == 4:
            self.image = pygame.image.load(CO.EN1_05_IMGPATH)
            self.change = 5

        elif self.change == 5:
            self.image = pygame.image.load(CO.EN1_06_IMGPATH)
            self.change = 6

        elif self.change == 6:
            self.image = pygame.image.load(CO.EN1_07_IMGPATH)
            self.change = 7

        elif self.change == 7:
            self.image = pygame.image.load(CO.EN1_01_IMGPATH)
            self.change = 0

    def change_en2(self):  # 控制角色动画
        if self.change == 0:
            self.image = pygame.image.load(CO.EN2_01_IMGPATH)
            self.change = 1

        elif self.change == 1:
            self.image = pygame.image.load(CO.EN2_02_IMGPATH)
            self.change = 2

        elif self.change == 2:
            self.image = pygame.image.load(CO.EN2_03_IMGPATH)
            self.change = 3

        elif self.change == 3:
            self.image = pygame.image.load(CO.EN2_04_IMGPATH)
            self.change = 0

    def change_enboos(self):  # 控制角色动画
        if self.change == 0:
            self.image = pygame.image.load(CO.EN_BOOS1_IMGPATH)
            self.change = 1

        elif self.change == 1:
            self.image = pygame.image.load(CO.EN_BOOS2_IMGPATH)
            self.change = 2

        elif self.change == 2:
            self.image = pygame.image.load(CO.EN_BOOS3_IMGPATH)
            self.change = 3

        elif self.change == 3:
            self.image = pygame.image.load(CO.EN_BOOS4_IMGPATH)
            self.change = 4

        elif self.change == 4:
            self.image = pygame.image.load(CO.EN_BOOS5_IMGPATH)
            self.change = 5

        elif self.change == 5:
            self.image = pygame.image.load(CO.EN_BOOS6_IMGPATH)
            self.change = 6

        elif self.change == 6:
            self.image = pygame.image.load(CO.EN_BOOS1_IMGPATH)
            self.change = 0

    def get_en_pos(self):  # 获得怪物的位置
        pos = self.rect.center
        return pos

    # 发射子弹方法
    def en_shoot(self):
        self.temp += 1
        if self.en_type =='3':
            if self.temp % 5 == 0:
                bullet = Bullet(self.en_bullet_img, (self.rect.top, self.rect.left))
                # 将子弹添加到子弹组中
                self.en_bullets.add(bullet)
        else:
            if self.temp % 30 == 0:
                bullet = Bullet(self.en_bullet_img, (self.rect.top,self.rect.left))
                # 将子弹添加到子弹组中
                self.en_bullets.add(bullet)
    def myKill(self):
        self.kill()


# 子弹
class Bullet(Sprite):
    # 构造方法，参数分别是子弹图片和起始位置
    def __init__(self, bullet_surface, bullet_init_pos):
        # 调用父类的构造方法
        Sprite.__init__(self)
        # 设置属性
        self.image = bullet_surface  # image属性：子弹图片
        self.rect = self.image.get_rect()  # rect属性：矩形
        self.rect.top = bullet_init_pos[0]  # 矩形左上角坐标
        self.rect.left = bullet_init_pos[1]  # 矩形左上角坐标
        self.speed = random.randint(-20,20) # speed属性：子弹移动速度
        self.speed1 = random.randint(-10,10) # speed属性：子弹移动速度
        self.temp = 0

    def en_bu_r(self):
        self.rect.left -= 20

    def en_bu_l(self):
        self.rect.left += 20

    # 子彈移动方法
    def update(self):
        self.rect.top += self.speed
        self.rect.left += self.speed1
        if self.rect.top <= 0 or self.rect.top >= CO.SCR_Y-200:
            self.kill()
        if self.rect.left <=100 or self.rect.left >= CO.SCR_X -200:
            self.kill()


class Bomb(Sprite):
    # 初始化爆炸
    def __init__(self):
        Sprite.__init__(self)
        # 加载爆炸资源

        self.image = [pygame.image.load(CO.EN1_BOOM_PATH + '/boom0' + str(v) + ".png") for v in range(1, 3)]
        # 设置当前爆炸播放索引
        self.index = 0
        # 图片爆炸播放间隔
        self.interval = 5
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


