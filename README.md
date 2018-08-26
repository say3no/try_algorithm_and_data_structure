# try Algorithm and Data Structure

This repository to learn the Algorithm and Data Structure for the Competitive Programming.

Text: [プログラミングコンテスト攻略のためのアルゴリズムとデータ構造 | 渡部 有隆, Ozy(協力), 秋葉 拓哉(協力)](https://www.amazon.co.jp/dp/4839952957/)


##  Textからの重要な引用
 - 重要なことは、プログラムを実装する前に、入力の上限からアルゴリズムの細作の計算量を評価することです。
 - 安定ソート(stable sort)とは、キーが２個以上含むようなデータをソートしたときに、処理の前後でそれらの要素の襦袢が変わらないようなアルゴリズム。
 - ソート選択は大事。計算量と安定性。
 
 
## 探索
### 線形探索
最悪でもO(N)。 

### 二分探索
運用の際は、sortにかかるコストも考えること。
 
### ハッシュ法
pythonではdict.


## データ構造
### 二分木 (Binary Tree)
- この数が0,1,2のいずれかである。
- *BTでは、左の子と右の子は厳密に区別される。*
- *二分木は、再帰的に定義することが出来る*

### 二十連鎖木
- [wikipedia: 二十連鎖木](https://ja.wikipedia.org/wiki/二重連鎖木)
- `p188_how_expression_tree.py`は二重連鎖木で解くと超高速にできる！と解説にあるのだが、いきなり二重連鎖木とかいわれてもわからん。
- TODO: あとで二重連鎖木での実装を書き直さないとね。

## 再帰と分割統治
再帰は分割統治法の一種。
> 1. 与えられた問題を部分問題に「分割」する
> 2. 部分問題を再帰的に解く
> 3. 得られた部分問題の書いを統合して、もとの問題を解く

## Dijkstra's algorithm
[ダイクストラ法 - Wikipedia](https://ja.wikipedia.org/wiki/ダイクストラ法)
 - グラフ理論における変の重みが皮膚数の場合の単一視点最短経路問題を解くための、再領有選択作によるアルゴリズム。
