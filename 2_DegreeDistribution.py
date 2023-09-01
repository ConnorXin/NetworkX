# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/7 13:01
# @File    :  2_DegreeDistribution.py
# @IDE     :  PyCharm

"""
常见度分布
泊松分布与幂律分布
"""
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # TODO 以 ER 随机网络为例的泊松分布
    # 创建一个 ER 随机网络
    n = 10000  # 节点为 10000、
    p = 0.001  # 连边概率为 0.001
    ER = nx.erdos_renyi_graph(n, p)
    # 获取平均度
    degreeER = dict(nx.degree(ER))
    degreeAver = sum(degreeER.values()) / len(ER.nodes)  # 10.538 由于是随即网络 结果具有随机性

    # 获取所有可能的度值对应的概率
    x = list(range(max(degreeER.values()) + 1))
    y = [i / n for i in nx.degree_histogram(ER)]
    # 绘制度分布
    plt.plot(x, y, 'ro-')
    plt.xlabel('$k$')
    plt.ylabel('$p_k$')
    plt.show()


    # TODO 以 BA 无标度网络为例的幂律分布
    # 创建 BA 无标度网络
    m = 3
    BA = nx.barabasi_albert_graph(n, m)
    degreeBA = dict(nx.degree(BA))
    degreeBAAver = sum(degreeBA.values()) / len(BA.nodes)

    # 获取所有可能的度值对应的概率
    x = list(range(max(degreeBA.values()) + 1))
    y = [i / n for i in nx.degree_histogram(BA)]

    # 绘制度分布
    plt.plot(x, y, 'ro-')
    plt.xlabel('$k$')
    plt.ylabel('$p_k$')
    plt.show()

    # 双坐标轴下显示
    plt.plot(x, y, 'ro-')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('$k$')
    plt.ylabel('$p_k$')
    plt.show()

    # 在双对数坐标轴下坐标值不能取0 不然无意义，因此需要将0排除掉
    new_x = []
    new_y = []
    for i in range(len(x)):
        if y[i] != 0:
            new_x.append(x[i])
            new_y.append(y[i])
    plt.plot(new_x, new_y, 'ro-')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('$k$')
    plt.ylabel('$p_k$')
    plt.show()