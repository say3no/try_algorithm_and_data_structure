# 10 Heap

優先度付きキューは二分探索木の応用で実現することができるが、バランスの良い木を保ちつつ効率k的な操作を行うには工夫が必要でその実装は簡単ではない。一方,**二分ヒープと呼ばれるデータ構造を用いれば比較的簡単に優先度付きキューを実装することができる**

## Requirement

 - Array
 - Quee
 - complete Binary Tree (すべてのnodeが同じ深さを持つ)
 - Binary Heap (木の各接点に割り当てられたキーが、一つの配列の各要素に対応した完全二分木)
 - Priority Quee


 ## Binary Heap

 論理的な構造は完全二分木だけれど、実際は１次元配列を用いて表す。この配列をA,二分ヒーpうのサイズをHとすれば、`hogehogefugafuga` で親、左の子、右の子を表現することができる。(あとでかく）
 j

 ## 10_2 完全二分木の Bin Heap 

http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_A&lang=jp


 ## 10_3 Max(Min) Bin Heap
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_B&lang=jp