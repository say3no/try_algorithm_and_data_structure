# try Algorithm and Data Structure

This repository to learn the Algorithm and Data Structure for the Competitive Programming.

Text: [プログラミングコンテスト攻略のためのアルゴリズムとデータ構造 | 渡部 有隆, Ozy(協力), 秋葉 拓哉(協力)](https://www.amazon.co.jp/dp/4839952957/)

[サポートページはここ](https://book.mynavi.jp/support/pc/5295/)


##  Textからの重要な引用
 - 重要なことは、プログラムを実装する前に、入力の上限からアルゴリズムの細作の計算量を評価することです。
 - 安定ソート(stable sort)とは、キーが２個以上含むようなデータをソートしたときに、処理の前後でそれらの要素の襦袢が変わらないようなアルゴリズム。
 - ソート選択は大事。計算量と安定性。
 

# Part 1 [準備編] プロコンで勝つための勉強法
## 1章 オンラインジャッジを活用しよう
みんな、会津大学が開発・運営する[AOJ](http://judge.u-aizu.ac.jp)をよろしくね。

# Part 2 [基礎編] プロコンのためのアルゴリズムとデータ構造
## 2章 アルゴリズムと計算量
## 3章 初頭的整列
## 4章 データ構造
## 5章 探索
### 線形探索
最悪でもO(N)。 

### 二分探索
運用の際は、sortにかかるコストも考えること。
 
### ハッシュ法
pythonではdict.
## 6章 再帰・分割統治法

## 再帰と分割統治
再帰は分割統治法の一種。
> 1. 与えられた問題を部分問題に「分割」する
> 2. 部分問題を再帰的に解く
> 3. 得られた部分問題の書いを統合して、もとの問題を解く

## 7章 高等的整列
様々なソート。pythonでは`numpy, math, scipy`が使えるのでイチから実装してスニペット(Dash)に登録しておく必要はない？

## ８章 木
完全に忘れている。学部２年の復習。

### 二分木 (Binary Tree)
- この数が0,1,2のいずれかである。
- *BTでは、左の子と右の子は厳密に区別される。*
- *二分木は、再帰的に定義することが出来る*

### 木の巡回
- p198_Tree_Walk.py
- O(n)ですべてのノードへアクセスできる
- ただし、再帰を使った実装を行うため、深すぎるとメモリの負担がすごくなる
- Pre_order. *左右のノードへ潜る前* に処理する。ポーランド記法であり、深さ優先探索である。
- In_order. 左のノードへ潜り、処理してから右のノードへ潜る。中置記法。
- Post_order. *左右のノードへ潜ってから*処理する。逆ポーランド記法。


### 順序木
 - 子に順序性がある木。二分木は順序木。

### 二十連鎖木
- [wikipedia: 二十連鎖木](https://ja.wikipedia.org/wiki/二重連鎖木)
- `p188_how_expression_tree.py`は二重連鎖木で解くと超高速にできる！と解説にあるのだが、いきなり二重連鎖木とかいわれてもわからん。
- TODO: あとで二重連鎖木での実装を書き直さないとね。

## 9章 二分探索木

 - 探索木(Search Tree)は、木構造(Tree)の一種。木探索(さっきやった)と探索木は別物なので注意。
 - wikipediaによれば、`探索木とは、計算機科学において特定のキーを特定するために仕様される木構造である。`
 - 有隆本によれば、`探索木は、挿入、検索、削除などの走査が行えるデータ構造で、辞書あるいは優先度付きキューとして用いることができます。`

### Binary Search Tree I



## 10章 ヒープ
## 11章 動的計画法
## 12章 グラフ
## 13章 重み付きグラフ

# Part 3 [応用編] プロコン必携ライブラリ
## 14章 高度なデータ構造
## 15章 高度なグラフアルゴリズム
## 16章 計算幾何学
## 17章 動的計画法
## 18章 整数論
## 17章 ヒューリスティック探索



# そのた
## 枝刈り
 - お気に入りのSlackチームの競プロチャンネルで、「枝刈りしてどうのこうの」という話を時折耳にしていた。枝刈りってなんだ？特別な説明を受けたわけではないが、今回、「これが枝刈りなのか」と悟った問題と出会った。
 それが、`p193_binary_tree.py`にある`def cal_height()`だ。これは、各ノードからleafに到達するために*最大*何手移動すればよいかを木における高さと定義し、これを探索する問題である。
 - 高さをrootから順に探査すると、深さが１つ増えるたびにその子々孫々すべての高さ候補を計算し、順位付けをしなければならない。
 - だが実際には高さはl,rいずれかの比較できまる。(あれ、これ大学2年の授業でやらなかったっけ…)
 - なので、全ての葉に対して根を目指して木を登ってもらう。各ノードを通過するときに、「高さ」の足跡を残してもらう。先約がいれば、その足跡の比較を行い、高さが高い方で上書きする。
 - その際、もし、先着のほうが値が大きければ、登頂を諦める。

## Dijkstra's algorithm
[ダイクストラ法 - Wikipedia](https://ja.wikipedia.org/wiki/ダイクストラ法)
 - グラフ理論における変の重みが皮膚数の場合の単一視点最短経路問題を解くための、再領有選択作によるアルゴリズム。
