# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/9 13:00
# @File    :  8_RegularNetwork.py
# @IDE     :  PyCharm

"""
常见的规则网络
"""
import warnings
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == '__main__':

    warnings.filterwarnings('ignore')

    n = 10

    # TODO 创建孤立节点
    G1 = nx.Graph()
    G1.add_nodes_from(list(range(n)))
    plt.figure(figsize = (4, 4))
    plt.title('signal node')
    nx.draw(G1, pos = nx.circular_layout(G1), node_size = 500, node_color = 'red', with_labels = True)
    plt.savefig('孤立图.pdf')

    # TODO 创建完全图
    G2 = nx.complete_graph(n)
    plt.figure(figsize = (4, 4))
    plt.title('full node')
    nx.draw(G2, pos = nx.circular_layout(G2), node_size = 500, node_color = 'red', with_labels = True)
    plt.savefig('完全图.pdf')

    # TODO 创建一维环状图
    G3 = nx.cycle_graph(n)
    plt.figure(figsize = (4, 4))
    plt.title('1-dimensional node')
    nx.draw(G3, pos = nx.circular_layout(G3), node_size = 500, node_color = 'red', with_labels = True)
    plt.savefig('一维环状图.pdf')

    # TODO K 近邻规则 (耦合) 图
    G4 = nx.watts_strogatz_graph(n, 4, 0)
    plt.figure(figsize = (4, 4))
    plt.title('K-Near Regulation')
    nx.draw(G4, pos = nx.circular_layout(G4), node_size = 500, node_color = 'red', with_labels = True)
    plt.savefig('K 近邻规则图.pdf')

    # TODO 二维方格图
    G5 = nx.grid_graph((6, 6), periodic = False)  # 设置二维边长为6
    plt.figure(figsize = (4, 4))
    plt.title('2-dimensional')
    nx.draw(G5, node_size = 500, node_color = 'red', with_labels = True)
    plt.savefig('二维方格图.pdf')