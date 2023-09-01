# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/7 14:06
# @File    :  4_clusterCoeff.py
# @IDE     :  PyCharm

"""
节点的集聚系数和平均集聚系数
"""
import networkx as nx


if __name__ == '__main__':

    G1 = nx.barabasi_albert_graph(1000, 3)

    # TODO 集聚系数
    # 返回每一个节点的集聚系数 类型是一个字典
    # 键是节点标签
    cluster = nx.clustering(G1)

    # TODO 平均集聚系数
    clusterAver = nx.average_clustering(G1)  # 0.02805750172599118

    # TODO 全局集聚系数
    clusterGlobal = nx.transitivity(G1)  # 0.0163503234520509
