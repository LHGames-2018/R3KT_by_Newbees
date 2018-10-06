# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:44:07 2018

@author: Sanae LOTFI
"""

import numpy as np

def fastest_path_estimation(start,all_nodes,weights):
    """
    Returns the time spent on the fastest path between 
    a given node "start" and all other nodes
    All_nodes must contain "start" also
    """
    lst_nodes = list(set(all_nodes) - set([start]))
    # nodes represents the minimal distance - at a given iteration - of each node to c
    nodes = {x:float("inf") for x in lst_nodes}
    nodes[start] = 0
    nodes_out = []
    
    min_dis_node = start
    while len(nodes_out)<len(all_nodes):
        for (node,value) in nodes.items():
            if node not in nodes_out:
                nodes[node] = min(value, nodes[min_dis_node]+weights[min_dis_node,node])
        nodes_out.append(min_dis_node)
        if len(nodes)!= len(nodes_out):
            min_dis_node = min({k : nodes[k] for k in set(nodes) - set(nodes_out) }, key=nodes.get)

    return nodes

# test:
    
# start = 0
# all_nodes = [0,1,2,3]
# weights=np.array([[0,7,3,6],[3,0,6,8],[1,2,0,1],[1,2,3,0]])
# print(fastest_path_estimation(start=start,
#                               all_nodes=all_nodes,
#                               weights=weights))