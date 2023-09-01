# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/9 14:57
# @File    :  9_CreateAlgorithm.py
# @IDE     :  PyCharm

"""
G(N, L)
G(N, p)
两种生成算法
"""
import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools


# TODO 编写算法程序
def GNL(N, L):
    """
    固定连边 L
    :param N: 节点数
    :param L: 连边数
    :return: G 生成随机图
    """
    G = nx.Graph()
    G.add_nodes_from(range(N))
    nlist = list(G)
    edge_count = 0
    while edge_count < L:
        # 生成随机连边
        u = random.choice(nlist)
        v = random.choice(nlist)
        if u == v or G.has_edge(u, v):
            continue
        else:
            G.add_edge(u, v)
            edge_count += 1

    return G


def GNP(N, p):
    """
    每对节点以概率 p 相连
    :param N: 节点数
    :param p: 相连概率
    :return: G 生成随机图
    """
    edges = itertools.combinations(range(N), 2)
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for e in edges:
        if random.random() < p:
            G.add_edge(*e)
    return G


if __name__ == '__main__':

    GNL = GNL(100, 200)
    GNP = GNP(100, 0.6)

    # plt.title('GNL')
    # nx.draw(GNL, node_size=100, with_labels=True)
    # plt.title('GNP')
    # nx.draw(GNP, node_size=100, with_labels=True)

    # TODO 直接调用 nx 中的包进行生成随机生成网络
    n, e, p = 20, 40, 0.2
    GNLnx = nx.gnm_random_graph(n, e)
    GNPnx = nx.gnp_random_graph(n, p)

    plt.figure(figsize = (8, 4))

    plt.subplot(121)
    nx.draw(GNLnx, pos = nx.circular_layout(GNLnx), node_size = 300, node_color = '#63ebe9', with_labels = True)
    plt.title('G(N, L)')

    plt.subplot(122)
    nx.draw(GNPnx, pos = nx.circular_layout(GNPnx), node_size = 300, node_color = '#63ebe9', with_labels = True)
    plt.title('G(N, p)')
