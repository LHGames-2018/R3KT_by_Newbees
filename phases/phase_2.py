# -*- coding: utf-8 -*-
from helper import *
from .phase_1 import move_home


def yolo_swag_phase_2(playerInfo, gameMap):
    if playerInfo.CarriedResources == playerInfo.CarryingCapacity:
        return create_move_action(DOWN)
    else:
        if gameMap.getTileAt(playerInfo.Position + UP) == TileContent.Wall:
            print('Wall at up')
            return create_attack_action(UP)
        if gameMap.getTileAt(playerInfo.Position + UP) == TileContent.House:
            print('House at up')
            return create_steal_action(UP)
        if gameMap.getTileAt(playerInfo.Position + UP) == TileContent.Resource:
            print('Ressouce at up')
            return create_collect_action(UP)
        return create_move_action(UP)