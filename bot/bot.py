from helper import *
from phases import *

action = None

mx, my = -1, -1


class Bot:
    def __init__(self):
        pass

    # def init_map(self):
    #     if mx == -1 and my == -1:
    #         for ()

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo
        print(self.PlayerInfo.CarriedResources)
        print(self.PlayerInfo.CarryingCapacity)
        # attrs = vars(playerInfo)
        # print(', '.join("%s: %s" % item for item in attrs.items()))

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        action = yolo_start(self.PlayerInfo, gameMap)
        return action
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        # return create_move_action(Point(-1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
