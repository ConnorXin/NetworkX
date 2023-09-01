# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/9 15:51
# @File    :  10_RandomNetworkDegreeDistribution.py
# @IDE     :  PyCharm

"""
随即网络的度分布
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats


def getDegreeDistribution(G, kmin, kmax):
    """
    定义求度分布函数
    :param G: 网络
    :param kmin: 最小值度
    :param kmax: 最大值度
    :return: 度以及相应的度分布概率
    """
    # 获取所有可能的度值
    k = list(range(kmin, kmax + 1))
    N = len(G.nodes())

    Pk = []
    for ki in k:
        c = 0
        for i in G.nodes():
            if G.degree(i) == ki:
                c += 1
        Pk.append(c / N)

    return k, Pk


if __name__ == '__main__':

    samples = 100  # 100个样本统计平均 使得样本与泊松分布更加吻合
    N = [100, 1000]  # 两个尺寸的 ER 网络

    # 偏于统计平均 指定区间 [20, 80]  平均度为50
    kmin, kmax, avk = 20, 80, 50
    s1 = np.zeros(kmax - kmin + 1)
    s2 = np.zeros(kmax - kmin + 1)

    for i in range(samples):
        ER1 = nx.gnp_random_graph(N[0], avk / N[0])
        x1, y1 = getDegreeDistribution(ER1, kmin, kmax)

        ER2 = nx.gnp_random_graph(N[1], avk / N[1])
        x2, y2 = getDegreeDistribution(ER2, kmin, kmax)

        s1 += np.array(y1)
        s2 += np.array(y2)


    # TODO 计算二项分布理论值
    n = 100
    p = 0.5
    k = np.arange(20, 81)
    pk_b = stats.binom.pmf(k, n, p)

    # TODO 计算泊松分布理论值
    pk_p = [np.exp(-avk) * (avk ** ki) / math.factorial(ki) for ki in range(kmin, kmax + 1)]


    # TODO 绘图对比
    plt.figure(figsize = (6, 4))
    plt.plot(x1, s1 / samples, 'ro', label = '$N = 100$')
    plt.plot(x2, s2 / samples, 'bs', label='$N = 1000$')
    plt.plot(x1, pk_b, 'g-', label='binomial')
    plt.plot(x2, pk_p, 'r-', label='poisson')
    plt.legend(loc = 0)
    plt.xlabel('$k$')
    plt.ylabel('$p_k$')
    plt.xlim([20, 80])
    plt.show()
