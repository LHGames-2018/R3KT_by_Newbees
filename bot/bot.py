from helper import *
from phases import *
from algos import *

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
        self.step = 0
        self.max_step = 100
        self.direction = None
        self.victimes = {}
        self.cpt_lvl = 0
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo
        # print(self.PlayerInfo.CarriedResources)
        # print(self.PlayerInfo.CarryingCapacity)

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

        # print('******')
        # # print(self.PlayerInfo.Position.x, self.PlayerInfo.Position.y)
        # d = fastest_path_estimation(Point(10, 5), self.PlayerInfo, gameMap)
        # direction = Point(d[0], d[1])
        # print(direction.x, direction.y)

        # print('*******')
        # return create_move_action(direction)

        # while not self.returned_home:
        #     if (self.PlayerInfo.Position == self.PlayerInfo.HouseLocation):
        #         self.returned_home = True
        #     else:
        #         return create_move_action(RIGHT)

        # return attack_if_you_can(self.PlayerInfo, gameMap)


        if self.cpt_lvl <= 10:
            self.cpt_lvl += 1
            return create_upgrade_action(UpgradeType.AttackPower)


        closest_player = get_closest_player(
            self.PlayerInfo.Position, visiblePlayers, self.victimes)
        if closest_player is not None and closest_player:
            attack = attack_if_you_can(self.PlayerInfo, gameMap)
            if attack is None:
                return go_to_dest(closest_player.Position.x, closest_player.Position.y, self.PlayerInfo, gameMap, True)
            elif attack is not None and closest_player.Name not in self.victimes:
                self.victimes[closest_player.Name] = 0.5
                return attack
            elif attack is not None and self.victimes[closest_player.Name] < 5.0:
                self.victimes[closest_player.Name] += 0.5
                return attack


        if self.step == 0 or self.direction is None:
            self.direction = get_random_direction()
        elif self.step == 100:
            self.step = 0
            self.direction = get_random_direction()

        self.step += 1
        return go_to_dest(self.direction.x, self.direction.y, self.PlayerInfo, gameMap, True)








        # return yolo_swag_phase_2(self.PlayerInfo, gameMap)

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        # return create_move_action(Point(-1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass


def get_closest_player(posi, visiblePlayers, victimes):
    min_dist = float('inf')
    closest_player = None
    target_victimes = [p for p in visiblePlayers if (p.Name not in victimes.keys() or (p.Name in victimes.keys() and victimes[p.Name] < 5.0)) ]
    for p in target_victimes:
        dist = math.sqrt((posi.x - p.Position.x)**2 +
                         (posi.y - p.Position.y)**2)
        if dist < min_dist and p.AttackPower < 5:
            min_dist = dist
            closest_player = p
    return closest_player


def go_to_dest(dx, dy, playerInfo, gameMap, add_random):
    if add_random:
        r = random.randint(0, 50)
        if r == 0:
            return create_move_action(get_random_direction())
    if dx < playerInfo.Position.x:
        if get_left_tile(playerInfo, gameMap) == TileContent.Wall:
            return create_attack_action(LEFT)
        if get_left_tile(playerInfo, gameMap) != TileContent.Empty and get_up_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(DOWN)
        elif get_left_tile(playerInfo, gameMap) != TileContent.Empty and get_down_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(UP)
        return create_move_action(LEFT)
    elif dx > playerInfo.Position.x:
        if get_right_tile(playerInfo, gameMap) == TileContent.Wall:
            return create_attack_action(RIGHT)
        if get_right_tile(playerInfo, gameMap) != TileContent.Empty and get_up_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(DOWN)
        elif get_right_tile(playerInfo, gameMap) != TileContent.Empty and get_down_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(UP)
        return create_move_action(RIGHT)
    elif dy < playerInfo.Position.y:
        if get_up_tile(playerInfo, gameMap) == TileContent.Wall:
            return create_attack_action(UP)
        if get_up_tile(playerInfo, gameMap) != TileContent.Empty and get_left_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(RIGHT)
        elif get_up_tile(playerInfo, gameMap) != TileContent.Empty and get_right_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(LEFT)
        return create_move_action(UP)
    elif dy > playerInfo.Position.y:
        if get_down_tile(playerInfo, gameMap) == TileContent.Wall:
            return create_attack_action(DOWN)
        if get_down_tile(playerInfo, gameMap) != TileContent.Empty and get_left_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(RIGHT)
        elif get_down_tile(playerInfo, gameMap) != TileContent.Empty and get_right_tile(playerInfo, gameMap) != TileContent.Empty:
            return create_move_action(LEFT)
        return create_move_action(DOWN)
    return create_empty_action()
