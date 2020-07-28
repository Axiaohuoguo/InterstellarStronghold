
import pygame

import source.setup
from source.constants import SCR_X ,SCR_Y,EN1_01_IMGPATH,OPEN_DOOR,OPEN_BULL,MU_ST_1


# stage = 0  # 游戏阶段
class Game:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.stage = 0
        self.enemy1_img = pygame.image.load(EN1_01_IMGPATH)
        self.tim = 0
        self.isEng = 0
        self.vPath = None
        self.temp = 0

    def run(self, state_0, state_1, player_1, en1s,en2s, en_boos, en_boom ,ends):
        pygame.key.set_repeat(60)  # 响应一直按下的键
        keep_going = True
        pygame.mixer.init()
        mu = pygame.mixer.music
        pygame.mixer.music.load(MU_ST_1)
        mu.play(-1)
        while keep_going:
            print("========玩家坐标",player_1.rect.topleft)
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
                 pass
            if self.stage == 1:  # 阶段 1
                if KEY_A:
                    player_1.change_p1()
                    player_1.pl_uodate_l()
                    if not state_1.get_lv_x() <=0:
                        en_boos.move_l()
                        for en_bu in en_boos.en_bullets:
                            en_bu.en_bu_l()
                        for en in en1s:
                            en.move_l()
                            for en_bu in en.en_bullets:
                                en_bu.en_bu_l()
                        for en in en2s:
                            en.move_l()
                            for en_bu in en.en_bullets:
                                en_bu.en_bu_l()

                        if en_boom.visible:
                            en_boom.en_boom_l()

                    state_1.map_update_r()
                if KEY_D:
                    if self.isEng != 0:
                        player_1.change_p1()
                        player_1.pl_uodate_r()
                    if not state_1.get_lv_x() >= 7680 and self.isEng == 0:
                        en_boos.move_r()
                        player_1.change_p1()
                        # player_1.pl_uodate_r()
                        for en_bu in en_boos.en_bullets:
                            en_bu.en_bu_r()
                        for en in en1s:
                            en.move_r()
                            for en_bu in en.en_bullets:
                                en_bu.en_bu_r()
                        for en in en2s:
                            en.move_r()
                            for en_bu in en.en_bullets:
                                en_bu.en_bu_r()


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

                if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击
                    if self.stage == 0:  # 阶段0
                        if (SCR_X // 2 - 554 // 2 <= mouse_x <= SCR_X // 2 + 554 // 2) and \
                                (SCR_Y // 2 <= mouse_y <= SCR_Y // 2 + 94):  # 判断鼠标是否在开始按钮之上
                            play_video(OPEN_DOOR,(SCR_X,SCR_Y))

                            pygame.mixer.music.load(MU_ST_1)
                            mu.play(-1)

                            self.stage = 1

            if self.stage == 0:  # 阶段 0 主菜单
                state_0.update(self.screen,pos)

            if self.stage == 1:  # 阶段 1 第一关
                if player_1.score1 >= 50:
                    player_1.bu_st = 1
                print("地图==：",state_1.lv_x_speed)
                if player_1.health <= 0 or (self.isEng != 0):
                    self.stage = 99
                state_1.map_loade(self.screen)  # 加载地图
                state_1.map_check()  # 检测地图
                player_1.player_load(self.screen)  # 加载玩家
                player_1.pl_check()
                player_1.draw_p1_health(self.screen)  # 玩家血条
                player_1.draw_score(self.screen)

                player_1.bullets.update()  # 绘制子弹
                player_1.bullets.draw(self.screen)  # 绘制角色子彈精灵组
                if self.isEng == 0:
                    self.screen.blit(en_boos.image, en_boos.rect)  # boos
                    en_boos.change_enboos()
                    en_boos.en_shoot()
                    en_boos.en_bullets.draw(self.screen)
                    en_boos.en_bullets.update()

                for en in en1s:  # 绘制敌人1
                    self.screen.blit(en.image, en.rect)
                    en.change_en1()
                    en.en_bullets.update()  # 绘制子弹
                    en.en_shoot()
                    en.en_bullets.draw(self.screen)  # 绘制怪物子彈精灵组

                for en in en2s:  # 绘制敌人2
                    self.screen.blit(en.image, en.rect)
                    en.change_en2()
                    en.en_bullets.update()  # 绘制子弹
                    en.en_shoot()
                    en.en_bullets.draw(self.screen)  # 绘制怪物子彈精灵组

                en_boom.draw(self.screen)
                en_boom.action()
                en1s.update()
                en2s.update()
                player_1.update()
                print("血量 ===",player_1.health)
                # 玩家和boos，boos子弹碰撞
                if pygame.sprite.collide_rect(player_1,en_boos):
                    player_1.health -= 50
                for boos_bu in en_boos.en_bullets :
                    if pygame.sprite.collide_rect(boos_bu,player_1):
                        player_1.health -= 20
                        boos_bu.kill()

                # 玩家子弹和敌人1碰撞
                self.tim += 1
                for en in en1s:
                    collide_list = pygame.sprite.spritecollide(player_1, en.en_bullets,True)
                    player_1.health -= (len(collide_list)*5)
                    if pygame.sprite.collide_rect(player_1,en): # 玩家和敌人碰撞
                        en.kill()
                        en_boom.set_pos(en.get_en_pos())
                        en_boom.visible = True
                        player_1.health -= 10
                    for bu in player_1.bullets:
                        if pygame.sprite.collide_mask(en, bu):
                            en.health -= 10  # 子弹伤害为10
                            bu.kill()
                            if en.health <= 0:
                                en_boom.set_pos(en.get_en_pos())
                                en_boom.visible = True
                                en.kill()
                                player_1.score1 += 10

                for bu in player_1.bullets:# 玩家子弹和 boos
                    if pygame.sprite.collide_rect(en_boos, bu) and self.isEng == 0:
                        en_boos.health -= 10
                        bu.kill()
                        if en_boos.health <= 0:
                            en_boom.set_pos(en_boos.get_en_pos())
                            en_boom.visible = True
                            player_1.score1 += 1000
                            self.isEng = -1
                # 玩家子弹和敌人2碰撞
                for en in en2s:
                    collide_list = pygame.sprite.spritecollide(player_1, en.en_bullets,True)
                    player_1.health -= (len(collide_list)*5)
                    if pygame.sprite.collide_rect(player_1,en): # 玩家和敌人碰撞
                        en.kill()
                        en_boom.set_pos(en.get_en_pos())
                        en_boom.visible = True
                        player_1.health -= 10

                    for bu in player_1.bullets:
                        if pygame.sprite.collide_mask(en, bu):
                            en.health -= 10  # 子弹伤害为10
                            bu.kill()
                            if en.health <= 0:
                                en_boom.set_pos(en.get_en_pos())
                                en_boom.visible = True
                                en.kill()
                                player_1.score1 += 10
                if self.isEng == 0:
                    for en_bu in en_boos.en_bullets: # boos zidan和角色碰撞
                        if pygame.sprite.collide_mask(en_bu,player_1):
                            player_1.health -= 10
                            en_bu.kill()

            if self.stage == 99:  # 阶段 99 游戏结束
                mu.stop()
                ends.update(self.screen)
                player_1.draw_score(self.screen)

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


from moviepy.editor import *

def play_video(path,size,pos = lambda t: (0, 0)):

    '''
    :param path:  路径
    :param size:  w，h大小
    :return:
    '''

    clip = VideoFileClip(path)
    clip.pos = pos
    clip.size=size
    clip.fps =60
    clip.mask = False
    clip.preview()


def close_video(clip):
    clip.close()


