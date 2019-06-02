# 12 Grapgh

> *コンピュータで扱う多くの問題は、「対象」とそれらの「関係」を抽象的に表したグラフと呼ばれるデータ構造で表すことができます。*

- 始点と終点が同じようなパスを閉路(cycle)という
- 閉路のない有向グラフをDirected Acyclic Graph(DAG)
- **グラフの最も基本的なアルゴリズムは探索**
- 代表的な探索アルゴリズムはDFSとBFS
- DFSは行けるところまでいく
- BFSは未探索の頂点の境界を幅一体に渡って拡張しながら探索します。*BFSは最短経路アルゴリズムの一つとして応用することができる。*

## 12_2 Graph

隣接行列を使う。

http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_A&lang=jp

 グラフの表現方法には、隣接リストによる表現と、隣接行列による表現があります。

## 12_3 Depth First Search


http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B&lang=jp

## 12_4 Breadth First Search

隣接行列を使う。

幅優先探索は、始点 `s` から `k + 1`の距離にある頂点を発見する前に、距離 `k` の頂点をすべて発見するので、**始点から各頂点までの最短距離を順番に求めることができます。**

http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=jp

## 12_5 Connected Components

連結成分。蘇州号データ構造と関連がある？ 隣接リストをつかう。

BFS,DFSはノードの数の自乗の計算量があるので、O(N^2)になる。グラフのサイズが大きくなると辛い。
メモリもいっぱいひつよう（当然）。ニューラルネットでもやったやん

>>> エッジの数が少ない疎なグラフでは、(隣接行列ではなく)隣接リストによる表現が適している。 次の図のように重み無し有向グラフを表す隣接リストでは、各頂点がその頂点に隣接する頂点の番号のリストを持つ。

http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_D&lang=jp

>> グラフの連結成分を求めるには、未訪問お頂点を始点としてDFSまたはBFSを繰り返す。この際、各探索ごとに異なる番号(色)を頂点に割り振ることで、指定された２つの頂点が同じグループ(色)に属するかをO(1)で調べることができます。