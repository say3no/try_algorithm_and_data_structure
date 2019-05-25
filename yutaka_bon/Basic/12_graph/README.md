# 12 Grapgh

> コンピュータで扱う多くの問題は、「対象」とそれらの「関係」を抽象的に表したグラフと呼ばれるデータ構造で表すことができます。

- 始点と終点が同じようなパスを閉路(cycle)という
- 閉路のない有向グラフをDirected Acyclic Graph(DAG)
- グラフの最も基本的なアルゴリズムは探索
- 代表的な探索アルゴリズムはDFSとBFS
- DFSは行けるところまでいく
- BFSは未探索の頂点の境界を幅一体に渡って拡張しながら探索します。*BFSは最短経路アルゴリズムの一つとして応用することができる。*

## 12_2 Graph

http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_A&lang=jp

 グラフの表現方法には、隣接リストによる表現と、隣接行列による表現があります。

## 12_3 Depth First Search

http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=jp

## 12_4 Breadth First Search

幅優先探索は、始点 `s` から `k + 1`の距離にある頂点を発見する前に、距離 `k` の頂点をすべて発見するので、**始点から各頂点までの最短距離を順番に求めることができます。**

http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=jp

## 12_5 