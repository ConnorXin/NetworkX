# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/7 13:51
# @File    :  3_NetworkStatisticCharacteristic.py
# @IDE     :  PyCharm

"""
网络的统计特征
1 网络的直径
2 网络的效率
3 网络的平均最短距离
"""
import networkx as nx


if __name__ == '__main__':

    # TODO 直径
    G1 = nx.barabasi_albert_graph(1000, 3)
    diameter = nx.diameter(G1)  # 6

    # TODO 指定节点对 i, j 之间的效率
    # 前提是这两个节点之间要有路径 即从 i >> j 是可达的
    # 比如从 1 >> 5 的效率
    # 效率等于最短距离长度的倒数
    efficient1_5 = nx.efficiency(G1, 1, 5)  # 0.5

    # TODO 最短距离长度
    shortest1_5 = nx.shortest_path_length(G1, 1, 5)  # 2

    # TODO 局部效率
    # 局部效率: 该节点的邻居引起的子图的平均全局效率
    # 平均局部效率: 每个节点的局部效率的平均值
    partEfficient = nx.local_efficiency(G1)  # 0.030939342885107878


    # TODO 全局效率
    # 图中所有节点对效率的平均值
    allEfficient = nx.global_efficiency(G1)  # 0.3018907907916223


    # TODO 整个网络的平均距离
    distanceAver = nx.average_shortest_path_length(G1)  # 3.504032032032032
