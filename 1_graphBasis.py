# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/1 13:38
# @File    :  1_graphBasis.py
# @IDE     :  PyCharm


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == '__main__':

    
    # TODO 简单图绘制
    # 创建一个空图 (不包含节点和边)
    G = nx.Graph()  # 无向图
    # 添加节点
    G.add_nodes_from([1, 2, 3, 4])
    # 添加边
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])
    # 可视化
    # nx.draw(G, node_size = 500, with_labels = True)

    # plt.show()
    
    
    # TODO 获取图的邻接矩阵
    # 获取图的边
    As = nx.adjacency_matrix(G)
    print(As)

    # 将边转换成二维数组形式的矩阵
    A = As.todense()


    # TODO 已知邻接矩阵 创建图
    arr = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
    A2G = nx.from_numpy_array(arr)
    # nx.draw(A2G, node_size=500, with_labels=True)

    # plt.show()


    # TODO 加权图
    WeightGra = nx.Graph()
    WeightGra.add_weighted_edges_from([(0, 1, 3.0), (1, 2, 7.5), (0, 2, 1.5)])
    # 获取边
    WEdge = nx.adjacency_matrix(WeightGra)
    # 邻接矩阵
    WMatrix = WEdge.todense()


    # TODO 有向图
    DirGra = nx.DiGraph()
    # 添加节点
    DirGra.add_nodes_from([1, 2, 3, 4])
    # 添加边
    DirGra.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])
    nx.draw(DirGra, node_size=500, with_labels=True)


    # TODO 度 平均度以及度分布
    DegreeGra = nx.Graph()  # 无向图
    # 添加节点
    DegreeGra.add_nodes_from([1, 2, 3, 4])
    # 添加边
    DegreeGra.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])
    nx.draw(DegreeGra, node_size=500, with_labels=True)

    # 获取网络的度
    degree = nx.degree(DegreeGra)
    degree = dict(degree)

    # 计算网络的平均度
    degreeAverage = np.sum(list(degree.values())) / len(DegreeGra.nodes)

    # 获取度分布
    freqlist = nx.degree_histogram(DegreeGra)  # 返回所有位于区间 [0, max(d)] 的度值的频率列表

    # TODO 绘制度分布直方图
    x = list(range(max(degree.values()) + 1))
    y = [i / len(DegreeGra.nodes) for i in freqlist]

    plt.bar(x, y, width = 0.5, color = 'red')
    plt.xlabel('$k$')
    plt.ylabel('$p_k$')
    plt.xlim([0, 4])
    plt.show()


    # TODO 路径和距离
    RouteGra = nx.Graph()
    RouteGra.add_nodes_from([1, 2, 3, 4, 5])
    RouteGra.add_edges_from([(1, 2), (2, 3), (2, 5), (3, 4), (4, 5)])
    nx.draw(RouteGra, node_size = 500, with_labels = True)

    # 1 >> 4 的最短路径
    shortestPath = nx.shortest_path(RouteGra, source = 1, target = 4)
    '''[1, 2, 3, 4]'''
    # 两个节点之间所有的最短路径
    allShortestPath = list(nx.all_shortest_paths(RouteGra, source = 1, target = 4))
    '''[[1, 2, 3, 4], [1, 2, 5, 4]]'''
    # 求两个节点的最短路径长度/距离
    shortestDistance = nx.shortest_path_length(RouteGra, source = 1, target = 4)
    '''3'''
    # 整个网络的平均距离
    networkDistanceAver = nx.average_shortest_path_length(RouteGra)
    '''1.6'''


    # TODO 连通性
    ConnectGra_1 = nx.Graph()
    ConnectGra_1.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    ConnectGra_1.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 7), (5, 6), (5, 7), (6, 7)])
    nx.draw(ConnectGra_1, node_size = 500, with_labels = True)

    ConnectGra_2 = nx.Graph()
    ConnectGra_2.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    ConnectGra_2.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (4, 7), (5, 6), (5, 7), (6, 7)])
    nx.draw(ConnectGra_2, node_size = 500, with_labels = True)

    # 判断是否连通
    print(nx.is_connected(ConnectGra_1))  # False
    print(nx.is_connected(ConnectGra_2))  # True


    # TODO 集聚系数
    ColumnGra = nx.Graph()
    ColumnGra.add_nodes_from([1, 2, 3, 4, 5])
    ColumnGra.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4),
                              (3, 5), (4, 5)])
    nx.draw(ColumnGra, node_size = 500, with_labels = True)
    nx.clustering(ColumnGra, 1)  # 1.0

    ColumnGra.remove_edges_from([(2, 4), (3, 4), (3, 5)])
    nx.draw(ColumnGra, node_size=500, with_labels=True)
    nx.clustering(ColumnGra, 1)  # 0.5

    ColumnGra.remove_edges_from([(2, 3), (2, 5), (4, 5)])
    nx.draw(ColumnGra, node_size=500, with_labels=True)
    nx.clustering(ColumnGra, 1)  # 0


    # TODO 平均集聚系数与全局集聚系数的区别
    ClusterGra = nx.Graph()
    ClusterGra.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
    ClusterGra.add_edges_from([(1, 2), (2, 3), (2, 4), (2, 5), (4, 5), (4, 6), (4, 7), (5, 7)])
    nx.draw(ClusterGra, node_size=500, with_labels=True)

    # 平均集聚系数
    Aver = nx.average_clustering(ClusterGra)  # 0.3095238095238095
    # 全局集聚系数
    Globle = nx.transitivity(ClusterGra)  # 0.375