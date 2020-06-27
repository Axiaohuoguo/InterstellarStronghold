import pygame
from moviepy.editor import *
import source.setup
from source.constants import SCR_X ,SCR_Y

# stage = 0  # 游戏阶段
class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.stage = 0

    def run(self, state_0, state_1,player_1):

        # self.play_video(videopath) # 播放视频
        # bulletFlag = False
        pygame.key.set_repeat(60)  # 响应一直按下的键
        keep_going = True
        while keep_going:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]
            for event in pygame.event.get():  # 获取事件列表
                if event.type == pygame.QUIT:  # 退出事件
                    keep_going = False
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                    if event.key == pygame.K_ESCAPE:
                        keep_going = False
                    if self.stage == 1:  # 阶段 1
                        if event.key == pygame.K_a:
                            player_1.change_p1()
                            state_1.map_update_r()
                        if event.key == pygame.K_d:
                            player_1.change_p1()
                            state_1.map_update_l()
                        if event.key == pygame.K_w:
                            player_1.change_p1()
                            player_1.pl_uodate_u()
                        if event.key == pygame.K_s:
                            player_1.change_p1()
                            player_1.pl_uodate_d()
                        if event.key == pygame.K_SPACE:
                            player_1.shoot()  # 发射子弹

                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()

                elif event.type == pygame.MOUSEBUTTONDOWN: # 鼠标点击
                    if self.stage == 0:  # 阶段0
                        if (mouse_x >= SCR_X // 2 - 554 // 2 and mouse_x <= SCR_X // 2 + 554 // 2) and \
                                (mouse_y >= SCR_Y // 2 and mouse_y <= SCR_Y // 2 + 94):  # 判断鼠标是否在开始按钮之上
                            self.stage = 1

            if self.stage == 0:  # 阶段 0 主菜单
                state_0.update(self.screen,pos)

            elif self.stage == 1 :  # 阶段 1 第一关
                state_1.map_loade(self.screen)  # 加载地图
                state_1.map_check() # 检测地图
                player_1.player_load(self.screen)
                player_1.pl_check()
                player_1.bullets.update()  # 绘制子弹
                player_1.bullets.draw(self.screen)  # 绘制精灵组

            print("游戏阶段 ", self.stage)

            pygame.display.update()
            self.clock.tick(60)  # 60帧
        pygame.quit()


def get_image(img, x, y, width, height, cloorkey, scale):
    '''
    :param img: 图片
    :param x: 方框左上x坐标
    :param y: 方框左上y坐标
    :param width: 方框的宽
    :param height: 方框的高
    :param cloorkey: 快速抠图底色
    :param scale: 放大倍数
    :return:
    '''
    images = pygame.Surface((width, height))  # 创建同大小空图
    images.blit(img, (0, 0), (x, y, width, height))  # 类似截图 后画图
    if cloorkey != 'NULL':
        images.set_colorkey(cloorkey)  # 快速抠图
    images = pygame.transform.scale(images, (int(width * scale), int(height * scale)))  # 缩放图片
    return images


def play_video(path,size):
    clip = VideoFileClip(path,)
    clip.reader.size=size
    clip.preview()


def close_video(clip):
    clip.close()



