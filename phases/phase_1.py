# -*- coding: utf-8 -*-
from helper import *
import random

def move_home(playerInfo, gameMap):
    r = random.randint(0,10)
    if r==0:
        return create_move_action(get_random_direction())
    if playerInfo.HouseLocation.x < playerInfo.Position.x:
        if get_left_tile(playerInfo, gameMap) != TileContent.Empty and get_up_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(DOWN)
        elif get_left_tile(playerInfo, gameMap) != TileContent.Empty and get_down_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(UP)
        return create_move_action(LEFT)
    elif playerInfo.HouseLocation.x > playerInfo.Position.x:
        if get_right_tile(playerInfo, gameMap) != TileContent.Empty and get_up_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(DOWN)
        elif get_right_tile(playerInfo, gameMap) != TileContent.Empty and get_down_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(UP)
        return create_move_action(RIGHT)
    elif playerInfo.HouseLocation.y < playerInfo.Position.y:
        if get_up_tile(playerInfo, gameMap) != TileContent.Empty and get_left_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(RIGHT)
        elif get_up_tile(playerInfo, gameMap) != TileContent.Empty and get_right_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(LEFT)
        return create_move_action(UP)
    elif playerInfo.HouseLocation.y > playerInfo.Position.y:
        if get_down_tile(playerInfo, gameMap) != TileContent.Empty and get_left_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(RIGHT)
        elif get_down_tile(playerInfo, gameMap) != TileContent.Empty and get_right_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(LEFT)
        return create_move_action(DOWN)
    print('AT HOME')
    return create_empty_action()


def yolo_start(playerInfo, gameMap):
    if playerInfo.CarriedResources >= 500:
        return move_home(playerInfo, gameMap)
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


def yolo_start_2(playerInfo, gameMap):
    if playerInfo.CarriedResources >= 500:
        return move_home(playerInfo, gameMap)
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
