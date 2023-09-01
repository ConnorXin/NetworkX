# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/8 17:20
# @File    :  7_CentralityIndicators.py
# @IDE     :  PyCharm

"""
常见中心性指标
"""
import matplotlib.pyplot as plt
import networkx as nx


if __name__ == '__main__':

    # 生成 ER 随机网络和 BA 无标度网络
    # 节点为100
    GER = nx.erdos_renyi_graph(100, 0.08)
    GBA = nx.barabasi_albert_graph(100, 4)

    # 绘图比较
    plt.figure(figsize=(10, 10))


    # TODO 度中心性
    degreeCenterER = nx.degree_centrality(GER)
    degreeCenterBA = nx.degree_centrality(GBA)

    plt.subplot(221)
    plt.plot(degreeCenterER.keys(), degreeCenterER.values(), 'ro', label = 'ER')
    plt.plot(degreeCenterBA.keys(), degreeCenterBA.values(), 'b--', label = 'BA')
    plt.legend(loc = 0)
    plt.xlabel('node label')
    plt.ylabel('degreeCenter')
    plt.title('degreeCentrality')

    # TODO 介数中心性
    betweennessCenterER = nx.betweenness_centrality(GER)
    betweennessCenterBA = nx.betweenness_centrality(GBA)

    plt.subplot(222)
    plt.plot(betweennessCenterER.keys(), betweennessCenterER.values(), 'ro', label='ER')
    plt.plot(betweennessCenterBA.keys(), betweennessCenterBA.values(), 'b--', label='BA')
    plt.legend(loc=0)
    plt.xlabel('node label')
    plt.ylabel('betweennessCente')
    plt.title('betweennessCentrality')

    # TODO 接近度中心性
    nearDegreeCenterER = nx.closeness_centrality(GER)
    nearDegreeCenterBA = nx.closeness_centrality(GBA)

    plt.subplot(223)
    plt.plot(nearDegreeCenterER.keys(), nearDegreeCenterER.values(), 'ro', label='ER')
    plt.plot(nearDegreeCenterBA.keys(), nearDegreeCenterBA.values(), 'b--', label='BA')
    plt.legend(loc=0)
    plt.xlabel('node label')
    plt.ylabel('nearDegreeCenter')
    plt.title('nearDegreeCentrality')

    # TODO 特征向量中心性
    characterCenterER = nx.eigenvector_centrality(GER)
    characterCenterBA = nx.eigenvector_centrality(GBA)

    plt.subplot(224)
    plt.plot(characterCenterER.keys(), characterCenterER.values(), 'ro', label='ER')
    plt.plot(characterCenterBA.keys(), characterCenterBA.values(), 'b--', label='BA')
    plt.legend(loc=0)
    plt.xlabel('node label')
    plt.ylabel('characterCenter')
    plt.title('characterCentrality')

    plt.show()
