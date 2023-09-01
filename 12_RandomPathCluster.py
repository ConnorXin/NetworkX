# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/10 17:41
# @File    :  12_RandomPathCluster.py
# @IDE     :  PyCharm

"""
随机网络的平均路径长度 集聚系数
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def cal_by_networkx(samples, N):
    """
    求解最短路径长度以及平均集聚系数
    相应的理论预测值
    :param samples:
    :param N:
    :return:
    """
    avl, clu = [], []
    t_avl, t_clu = [], []
    for n in N:
        p = 10 / n
        avl0 = 0
        clu0 = 0
        t_avl0 = 0
        t_clu0 = 0
        for i in range(samples):
            Ger = nx.gnp_random_graph(n,p)
            avk = sum([Ger.degree(j) for j in Ger.nodes()]) / n
            # 理论近似值
            t_avl0 += np.log(n) / np.log(avk)
            t_clu0 += avk / n

            # 模拟值
            # 如果Ger是连通的
            if nx.is_connected(Ger):
                avl0 += nx.average_shortest_path_length(Ger)
            else: # 如果Ger是不连通的，用最大连通子图的平均距离代替整个网络的平均距离
                Gcc = sorted(nx.connected_components(Ger), key=len, reverse=True)
                # 得到图Ger的最大连通组件
                LCC = Ger.subgraph(Gcc[0])
                avl0 += nx.average_shortest_path_length(LCC)

            clu0 += nx.average_clustering(Ger)
        avl.append(avl0 / samples)
        clu.append(clu0 / samples)
        t_avl.append(t_avl0 / samples)
        t_clu.append(t_clu0/samples)
    return avl, clu, t_avl, t_clu


if __name__ == '__main__':

    samples = 1  # 为了更精确 通常将样本设置的大一些
    N = [100, 200, 300, 500, 700, 1000, 2000, 5000]
    avl_0, clu_0, t_avl0, t_clu0 = cal_by_networkx(samples, N)

    plt.figure(figsize=(10, 4))
    plt.subplot(121)
    plt.plot(N, avl_0, 'ro', label='simulation')
    plt.plot(N, t_avl0, 'r--', label='theory predicts')
    plt.title("average path length")
    plt.legend(loc=0)
    plt.xlabel("$N$")
    plt.ylabel("$<l>$")
    plt.xscale("log")

    plt.subplot(122)
    plt.plot(N, clu_0, 'ro', label='simulation')
    plt.plot(N, t_clu0, 'r--', label='theory predicts')
    plt.title("average clustering")
    plt.legend(loc=0)
    plt.xlabel("$N$")
    plt.ylabel("$<C>$")
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
