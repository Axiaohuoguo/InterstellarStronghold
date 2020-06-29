from source import tools
from source.states import main_menu,maps
from source.component import player,enemy
from source.constants import SRC_SIZE ,ST_VIDEOPATH


def main():
    game = tools.Game()
    states_0 = main_menu.MainMenu()  # 主菜单
    states_1 = maps.MapCon()  # 地图控制
    p1 = player.PlayerCO()
    en1 = enemy.Enemy()

    # tools.play_video(ST_VIDEOPATH,SRC_SIZE)
    game.run(states_0,states_1,p1,en1)


if __name__ == '__main__':
    main()
