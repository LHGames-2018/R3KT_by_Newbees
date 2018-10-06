# -*- coding: utf-8 -*-
from helper import *


def move_home(playerInfo):
    if playerInfo.HouseLocation.x < playerInfo.Position.x:
        return create_move_action(LEFT)
    elif playerInfo.HouseLocation.x > playerInfo.Position.x:
        return create_move_action(RIGHT)
    elif playerInfo.HouseLocation.y < playerInfo.Position.y:
        return create_move_action(UP)
    elif playerInfo.HouseLocation.y > playerInfo.Position.y:
        return create_move_action(DOWN)
    print('AT HOME')
    return create_empty_action()


def yolo_start(playerInfo, gameMap):
    if playerInfo.CarriedResources >= 500:
        return move_home(playerInfo)
    # elif playerInfo.CarriedResources != 0 and playerInfo.Position.x == playerInfo.HouseLocation.x and playerInfo.Position.y == playerInfo.HouseLocation.y:
    #     return create_empty_action()
    else:
        if gameMap.getTileAt(playerInfo.Position + UP) == TileContent.Resource:
            print('Ressouce at up')
            return create_collect_action(UP)
        elif gameMap.getTileAt(playerInfo.Position + DOWN) == TileContent.Resource:
            print('Ressouce at down')
            return create_collect_action(DOWN)
        elif gameMap.getTileAt(playerInfo.Position + LEFT) == TileContent.Resource:
            print('Ressouce at left')
            return create_collect_action(LEFT)
        elif gameMap.getTileAt(playerInfo.Position + RIGHT) == TileContent.Resource:
            print('Ressouce at right')
            return create_collect_action(RIGHT)
        else:
            print('Move randomly')
            return create_move_action(get_random_direction())


def discover_map():
    print('Phase_1')
