from source import tools
from source.constants import EN1_JSONPATH,ST_VIDEOPATH,SRC_SIZE

from source.states import main_menu,maps
from source.component import player,enemys
import json
import pygame.sprite as sprite


def play_video():
    tools.play_video(ST_VIDEOPATH, SRC_SIZE)


def main():
    game = tools.Game()
    states_0 = main_menu.MainMenu()  # 主菜单
    states_1 = maps.MapCon()  # 地图控制
    p1 = player.PlayerCO('1')

    file =open(EN1_JSONPATH,'r', encoding='UTF-8')
    data=json.load(file)
    en1s = sprite.Group()
    for i in data['enemy_01']:
        print(i)
        en1s.add(enemys.Enemys(i["X"], i["Y"],'1'))
    en2s = sprite.Group()
    for i in data['enemy_02']:
        print(i)
        en2s.add(enemys.Enemys(i["X"], i["Y"],'2'))

    en_boom = enemys.Bomb()
    game.run(states_0,states_1,p1,en1s,en2s,en_boom)


if __name__ == '__main__':
    try:
        if callable(play_video()):
            play_video()
        main()
    except:
        print("ex")
    else:
        print("==")

