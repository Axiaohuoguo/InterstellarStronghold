from source import tools
from source.states import main_menu,maps
from source.component import player,enemys
from source.constants import EN1_JSONPATH
import json
import pygame.sprite as Sprite
def main():

    game = tools.Game()
    states_0 = main_menu.MainMenu()  # 主菜单
    states_1 = maps.MapCon()  # 地图控制
    p1 = player.PlayerCO('1')
    file =open(EN1_JSONPATH,'r', encoding='UTF-8')
    data=json.load(file)
    en1s = Sprite.Group()
    for i in data['enemy_01']:
        print(i)
        en1s.add(enemys.Enemys(i["X"], i["Y"],'1'))
    # # tools.play_video(ST_VIDEOPATH,SRC_SIZE)
    en_boom = enemys.Bomb()
    game.run(states_0,states_1,p1,en1s,en_boom)


if __name__ == '__main__':
    main()
