# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:44:07 2018

@author: Sanae LOTFI
"""
from helper import *


def get_weights(end_position, playerInfo, gameMap):
    edges = []
    start_node = (playerInfo.Position.x, playerInfo.Position.y)
    end_node = (end_position.x, end_position.y)
    # creating edges horizotally
    range_x = abs(end_node[0] - start_node[0])
    range_y = abs(end_node[1] - start_node[1])
    min_x = min(end_node[0], start_node[0])
    min_y = min(end_node[1], start_node[1])
    for j in range(range_y):
        for i in range(range_x):
            if gameMap.getTileAt(Point(min_x+i+1, min_y+j)) == TileContent.Empty:
                edges.append(((min_x+i, min_y+j), (min_x+i+1, min_y+j)))
                edges.append(((min_x+i+1, min_y+j), (min_x+i, min_y+j)))
    # creating edges vertically
    for i in range(range_x):
        for j in range(range_y):
            if gameMap.getTileAt(Point(min_x+i, min_y+j+1)) == TileContent.Empty:
                edges.append(((min_x+i, min_y+j), (min_x+i, min_y+j+1)))
                edges.append(((min_x+i, min_y+j+1), (min_x+i, min_y+j)))
    return edges


def fastest_path_estimation(end_position, playerInfo, gameMap):
    """
    Returns the time spent on the fastest path between
    a given node "start" and all other nodes
    All_nodes must contain "start" also
    """

    edges = get_weights(end_position, playerInfo, gameMap)

    end_node = (end_position.x, end_position.y)
    start_node = (playerInfo.Position.x, playerInfo.Position.y)
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
    all_nodes = list(nodes)
    lst_nodes = list(set(all_nodes) - set([start_node]))
    # nodes represents the minimal distance - at a given iteration - of each node to c
    nodes = {x: float("inf") for x in lst_nodes}
    nodes[start_node] = 0
    nodes_out = []
    min_dis_node = start_node
    while min_dis_node != end_node:
        next_nodes = [(min_dis_node[0]+1, min_dis_node[1]),
                      (min_dis_node[0]-1, min_dis_node[1]),
                      (min_dis_node[0], min_dis_node[1]+1),
                      (min_dis_node[0], min_dis_node[1]-1)]
        for node in next_nodes:
            print (nodes)
            value = nodes[node]
            if node not in nodes_out:
                nodes[node] = min(value, nodes[min_dis_node]+1)
        nodes_out.append(min_dis_node)
        if len(nodes) != len(nodes_out):
            min_dis_node = min({k: nodes[k] for k in set(
                nodes) - set(nodes_out)}, key=nodes.get)
    path = []
    current_node = end_node
    path.append(current_node)
    while current_node != start_node:
        neighbors = [(current_node[0]+1, current_node[1]),
                    (current_node[0]-1, current_node[1]),
                    (current_node[0], current_node[1]+1),
                    (current_node[0], current_node[1]-1)]
        current_node = (min({k: nodes[k] for k in neighbors}, key=nodes.get))
        path.append(current_node)
    
    return path[-1]


def totototoo(playerInfo, gameMap):
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
