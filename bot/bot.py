from helper import *
from phases import *

# action = None

# mx, my = -1, -1

# def get_rayon(x, y):
#     return math.sqrt(math.pow(x, 2)+math.pow(y.2))

# def search_mine(playerInfo, gameMap):
#     for i in range(playerInfo.HouseLocation.x-9, playerInfo.HouseLocation.x+9):
#         for j in range(playerInfo.HouseLocation.y-9, playerInfo.HouseLocation.y+9):
#             if gameMap.getTileAt(Point(i, j)) == TileContent.Resource:
#                 if get_rayon()

# def init_map(playerInfo, gameMap):
#     if mx != -1 and my != -1:
#         if gameMap.getTileAt(Point(mx, my)) != TileContent.Resource:
#             search_mine(playerInfo, gameMap)
#     if mx == -1 and my == -1:
#         for ()


class Bot:
    def __init__(self):
        self.returned_home = False
        self.hx, self.hy = None, None
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        if self.hx is None and self.hy is None:
            self.hx, self.hy = playerInfo.HouseLocation.x, playerInfo.HouseLocation.y
        self.PlayerInfo = playerInfo
        print(self.PlayerInfo.CarriedResources)
        print(self.PlayerInfo.CarryingCapacity)

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        # while not self.returned_home :
        #     if (self.PlayerInfo.Position == self.PlayerInfo.HouseLocation):
        #         self.returned_home = True
        #     return move_home(self.PlayerInfo, gameMap, False, self.hx, self.hy)
        # action = yolo_swag_phase_2(self.PlayerInfo, gameMap)
        # print(self.PlayerInfo.HouseLocation)
        # print(self.PlayerInfo.Position)
        # return action

        return create_attack_action(LEFT)

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        # return create_move_action(Point(-1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
