# vim: set fileencoding=utf-8 :
"""
https://imoz.jp/algorithms/imos_method.html
いもす法の練習。
累積和のアルゴリズムを多次元、多次数に拡張したもの。

あなたはお店の経営者で、開店時刻 t ∋ [0,T] において、C人の客が入店・退店を行った。
この時、 区間 t における瞬間最大来客数を M とする。Mを求めよ。
"""


def main():
    C = input()  # 訪れた客の総数
    T = input()  # 閉店時刻
    io = [0] * T  # いもす法では、全時刻での入店・退店処理を記憶しておく。
    num = [0] * T  # いもす法では、全時刻での入店・退店処理を記憶しておく。
    c = [map(int, raw_input().split()) for _ in xrange(C)]  # [0]=>入店時刻 S_i [1]=>退店時刻 E_i
    for ele in c:
        io[ele[0]] += 1
        io[ele[1]] -= 1

    # ioについて累積和を計算する。これが、各時刻 t ∋ [0,T] における来店者数と一致する(マジ？！）
    for i in xrange(0, T):
        num[i] = num[i - 1] + io[i]

    print(max(num))


if __name__ == "__main__":
    main()

"""
TEST:
8
10
1 6
2 7
0 3
1 9
4 6
8 9
5 8
2 4
"""
