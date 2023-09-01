# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/10 16:14
# @File    :  11_RealNetworkDegreeDistribution.py
# @IDE     :  PyCharm

"""
真实网络的度分布
"""
import numpy as np
import pandas as pd
import networkx as nx
from decimal import Decimal
import matplotlib.pyplot as plt


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

    # 加载三个真实网络
    # 互联网络
    internet = pd.read_table('./巴拉巴西网络科学书中数据集/datasets/internet.txt.')
    internet.columns = ['source', 'target']
    GInternet = nx.from_pandas_edgelist(internet, 'source', 'target', create_using = nx.Graph())
    # 引文网络
    citation = pd.read_csv('./citation.csv')
    GCitation = nx.from_pandas_edgelist(citation, 'source', 'target', create_using = nx.Graph())
    # 蛋白质交互网络
    protein = pd.read_csv('./protein_interaction.csv')
    GProtein = nx.from_pandas_edgelist(protein, 'source', 'target', create_using = nx.Graph())

    # 查看网络规模
    print(len(GInternet.nodes()))  # 192244
    print(len(GCitation.nodes()))  # 23133
    print(len(GProtein.nodes()))  # 2018

    # 获取网络的度
    degInternet = [GInternet.degree(i) for i in GInternet.nodes()]
    degCitation = [GCitation.degree(i) for i in GCitation.nodes()]
    degProtein = [GProtein.degree(i) for i in GProtein.nodes()]

    # 度的最值
    degMaxInternet, degMinInternet = max(degInternet), min(degInternet)
    degMaxCitation, degMinCitation = max(degCitation), min(degCitation)
    degMaxProtein, degMinProtein = max(degProtein), min(degProtein)

    # 度分布函数
    kInternet, PkInternets = getDegreeDistribution(GInternet, degMinInternet, degMaxInternet)
    kCitation, PkCitations = getDegreeDistribution(GCitation, degMinCitation, degMaxCitation)
    kProtein, PkProteins = getDegreeDistribution(GProtein, degMinProtein, degMaxProtein)

    # 绘制度分布
    avkInternet = sum(degInternet) / len(GInternet.nodes())
    avkCitation = sum(degCitation) / len(GCitation.nodes())
    avkProtein = sum(degProtein) / len(GProtein.nodes())

    # 计算每个网络的平均度度值 以此绘制泊松分布
    # 使用以下方法可能会报错：OverflowError: int too large to convert to float
    # pk_p1 = [np.exp(-avk1)*(avk1**ki)/math.factorial(ki) for ki in range(kmin1, kmax1+1)]
    # pk_p2 = [np.exp(-avk2)*(avk2**ki)/math.factorial(ki) for ki in range(kmin2, kmax2+1)]
    # pk_p3 = [np.exp(-avk3)*(avk3**ki)/math.factorial(ki) for ki in range(kmin3, kmax3+1)]
    pkInternet = [Decimal(np.exp(-avkInternet)) * (Decimal(avkInternet) ** Decimal(ki)) / Decimal(np.math.factorial(ki))
                  for ki in range(degMinInternet, degMaxInternet + 1)]
    pkCitation = [Decimal(np.exp(-avkCitation)) * (Decimal(avkCitation) ** Decimal(ki)) / Decimal(np.math.factorial(ki))
                  for ki in range(degMinCitation, degMaxCitation + 1)]
    pkProtein = [Decimal(np.exp(-avkProtein)) * (Decimal(avkProtein) ** Decimal(ki)) / Decimal(np.math.factorial(ki))
                 for ki in range(degMinProtein, degMaxProtein + 1)]

    # 绘制度分布
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.plot(kInternet, PkInternets, 'ro', label='Internet')
    plt.plot(list(range(degMinInternet, degMaxInternet + 1)), pkInternet, 'g-', label='poisson')
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.ylabel("$p_k$")
    plt.ylim([1e-6, 1])
    plt.xscale("log")
    plt.yscale("log")

    plt.subplot(132)
    plt.plot(kCitation, PkCitations, 'ro', label='collaboration')
    plt.plot(list(range(degMinCitation, degMaxCitation + 1)), pkCitation, 'g-', label='poisson')
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.ylabel("$p_k$")
    plt.ylim([1e-5, 1])
    plt.xscale("log")
    plt.yscale("log")

    plt.subplot(133)
    plt.plot(kProtein, PkProteins, 'ro', label='protein')
    plt.plot(list(range(degMinProtein, degMaxProtein + 1)), pkProtein, 'g-', label='poisson')
    plt.legend(loc=0)
    plt.xlabel("$k$")
    plt.ylabel("$p_k$")
    plt.ylim([1e-4, 1])
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
