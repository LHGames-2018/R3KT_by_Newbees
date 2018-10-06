# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 12:32:48 2018

@author: Sanae LOTFI
"""

from helper import *


class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        mapped_zone = {}
        current_position = self.Position
        explore = True
        next_position = get_random_direction()
        value_position = getTileAt(self, next_position)
        mapped_zone[next_position] = value_position
        if value_position == 4:
            create_collect_action(next_position)
            
            
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass