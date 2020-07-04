import pygame
from moviepy.editor import *
import source.setup
from source.constants import SCR_X ,SCR_Y,ST_SOUND,EN1_01_IMGPATH,EN1_02_IMGPATH,EN1_03_IMGPATH,EN1_04_IMGPATH


# stage = 0  # 游戏阶段
class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.stage = 0
        self.enemy1_img = pygame.image.load(EN1_01_IMGPATH)
        self.tim = 0

    def run(self, state_0, state_1, player_1, en1s, en_boom):
        pygame.key.set_repeat(60)  # 响应一直按下的键
        keep_going = True

        while keep_going:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]
            mouse_y = pos[1]

            KEY_ESCAPE = pygame.key.get_pressed()[pygame.K_ESCAPE]
            KEY_A = pygame.key.get_pressed()[pygame.K_a]
            KEY_D = pygame.key.get_pressed()[pygame.K_d]
            KEY_W = pygame.key.get_pressed()[pygame.K_w]
            KEY_S = pygame.key.get_pressed()[pygame.K_s]
            KEY_SPACE = pygame.key.get_pressed()[pygame.K_SPACE]
            if KEY_ESCAPE:
                keep_going = False
            if self.stage == 1:  # 阶段 1
                if KEY_A:
                    player_1.change_p1()
                    player_1.pl_uodate_l()
                    for en in en1s:
                        en.move_l()
                    if en_boom.visible:
                        en_boom.en_boom_l()

                    state_1.map_update_r()
                if KEY_D:
                    player_1.change_p1()
                    player_1.pl_uodate_r()
                    for en in en1s:
                        en.move_r()
                    if en_boom.visible:
                        en_boom.en_boom_r()

                    state_1.map_update_l()
                if KEY_W:
                    player_1.change_p1()
                    player_1.pl_uodate_u()

                if KEY_S:
                    player_1.change_p1()
                    player_1.pl_uodate_d()
                if KEY_SPACE:
                    player_1.shoot()  # 发射子弹

            for event in pygame.event.get():  # 获取事件列表
                if event.type == pygame.QUIT:  # 退出事件
                    keep_going = False
                # if event.type == pygame.KEYDOWN:
                #     self.keys = pygame.key.get_pressed()
                # if event.type == pygame.KEYUP:
                #     self.keys = pygame.key.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN: # 鼠标点击
                    if self.stage == 0:  # 阶段0
                        if (mouse_x >= SCR_X // 2 - 554 // 2 and mouse_x <= SCR_X // 2 + 554 // 2) and \
                                (mouse_y >= SCR_Y // 2 and mouse_y <= SCR_Y // 2 + 94):  # 判断鼠标是否在开始按钮之上
                            self.stage = 1

            if self.stage == 0:  # 阶段 0 主菜单
                state_0.update(self.screen,pos)

            if self.stage == 1:  # 阶段 1 第一关
                state_1.map_loade(self.screen)  # 加载地图
                state_1.map_check()  # 检测地图

                player_1.player_load(self.screen)  # 加载玩家
                player_1.pl_check()

                player_1.bullets.update()  # 绘制子弹
                player_1.bullets.draw(self.screen)  # 绘制精灵组

                for en in en1s:  # 绘制敌人
                    self.screen.blit(en.image, en.rect)
                    en.change_en1()

                # en_boom.set_pos(en.get_en_pos())

                en_boom.draw(self.screen)
                en_boom.action()

                # 子弹和敌人碰撞
                self.tim += 1
                for en in en1s:
                    for bu in player_1.bullets:
                        if pygame.sprite.collide_mask(en, bu):
                            en.health -= 10  # 子弹伤害为10
                            bu.kill()
                            if en.health <= 0:
                                en_boom.set_pos(en.get_en_pos())
                                en_boom.visible = True
                                en.kill()




                    # en1gs.add(en)
                    # if pygame.sprite.collide_mask(player_1,en):
                    #     print('----')

                # if pygame.sprite.collide_mask(player_1, en):
                #     print("-------")
                # print("en",en.en1_rect)
                # for bu in player_1.bullets:
                #     print(bu)
                    # for bu in player_1.bullets:
                    #     if pygame.sprite.collide_circle(bu,en.en1_rectdw):
                    #         print("-------------")

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



