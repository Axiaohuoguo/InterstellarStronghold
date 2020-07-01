from source import tools
from source.states import main_menu,maps
from source.component import player,enemys
from source.constants import EN1_JSONPATH
import json

def main():

    game = tools.Game()
    states_0 = main_menu.MainMenu()  # 主菜单
    states_1 = maps.MapCon()  # 地图控制
    p1 = player.PlayerCO()
    file =open(EN1_JSONPATH,'r', encoding='UTF-8')
    data=json.load(file)
    en1s = []
    for i in data['enemy_01']:
        print(i)
        en1s.append(enemys.Enemys(i["X"], i["Y"]))
    # # tools.play_video(ST_VIDEOPATH,SRC_SIZE)

    game.run(states_0,states_1,p1,en1s)


if __name__ == '__main__':
    main()
