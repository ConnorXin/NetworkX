# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/7 14:12
# @File    :  5_degree_degreeRelevance.py
# @IDE     :  PyCharm

"""
度-度相关性
1 基于最近邻平均度值的度-度相关性
2 基于 Pearson 相关系数的度-度相关性
"""
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


def averageNearestNeighborDegree(G):
    """
    基于最近邻平均都的度-度相关性
    求解最近邻平均度
    :param G: 网络
    :return:
    """
    # 获取所有可能的度值
    k = set([G.degree(i) for i in G.nodes()])
    sorted_k = sorted(k)

    # 求解所有度值对应的近邻平均度
    k_nn_k = []
    for ki in sorted_k:
        c = 0
        k_nn_i = 0
        for i in G.nodes():
            if G.degree(i) == ki:
                k_nn_i += sum([G.degree(j) for j in list(nx.all_neighbors(G, i))]) / ki
                c += 1
        k_nn_k.append(k_nn_i / c)

    return sorted_k, k_nn_k


if __name__ == '__main__':

    # 三个真实数据集
    # 1 科学合作网络
    df1 = pd.read_csv('./citation.csv')
    G1 = nx.from_pandas_edgelist(df1, 'source', 'target', create_using = nx.Graph())
    # 2 电网
    df2 = pd.read_csv('./power.csv')
    G2 = nx.from_pandas_edgelist(df2, 'source', 'target', create_using = nx.Graph())
    # 3 代谢网络
    df3 = pd.read_csv('./celegans_metabolic.csv')
    G3 = nx.from_pandas_edgelist(df3, 'source', 'target', create_using = nx.Graph())


    # TODO 基于 Pearson 相关系数的度-度相关性
    # 计算三个网络的关联系数
    r1 = nx.degree_assortativity_coefficient(G1)
    r2 = nx.degree_assortativity_coefficient(G2)
    r3 = nx.degree_assortativity_coefficient(G3)
    '''
    r1 = 0.13506886900042142 > 0 说明网络是正相关的
    r2 = 0.0034569877442048825 无限接近于0 说明第二个网络是近似无关联
    r3 = -0.219662309363656 < 0 说明网络是负相关的
    '''

    # Pearson 相关系数
    r1 = nx.degree_pearson_correlation_coefficient(G1)
    r2 = nx.degree_pearson_correlation_coefficient(G2)
    r3 = nx.degree_pearson_correlation_coefficient(G3)
    '''
    与关联系数几乎一样
    r1 = 0.13506886900042694 > 0 说明网络是正相关的
    r2 = 0.0034569877442049216 无限接近于0 说明第二个网络是近似无关联
    r3 = -0.21966230936365555 < 0 说明网络是负相关的
    '''

    # TODO 通过最近邻平均度绘制度值与最近邻平均度的关系
    x1, y1 = averageNearestNeighborDegree(G1)
    x2, y2 = averageNearestNeighborDegree(G2)
    x3, y3 = averageNearestNeighborDegree(G3)

    plt.figure(figsize = (12, 4))
    plt.subplot(131)
    plt.plot(x1, y1, 'ro', label = 'r = ' + '%.4f' % r1)
    plt.legend(loc = 0)
    plt.xlabel('$k$')
    plt.ylabel('$k_{nn}(k)$')
    plt.xscale('log')
    plt.ylabel('log')
    plt.title('citation')
    plt.ylim([1, 100])

    plt.subplot(132)
    plt.plot(x2, y2, 'bs', label = 'r = ' + '%.4f' % r2)
    plt.legend(loc = 0)
    plt.xlabel('$k$')
    plt.ylabel('$k_{nn}(k)$')
    plt.xscale('log')
    plt.ylabel('log')
    plt.title('power')
    plt.ylim([1, 10])

    plt.subplot(133)
    plt.plot(x3, y3, 'gv', label = 'r = ' + '%.4f' % r3)
    plt.legend(loc = 0)
    plt.xlabel('$k$')
    plt.ylabel('$k_{nn}(k)$')
    plt.xscale('log')
    plt.ylabel('log')
    plt.title('celegans_metabolic')
    plt.ylim([1, 100])

    plt.tight_layout()
    plt.show()