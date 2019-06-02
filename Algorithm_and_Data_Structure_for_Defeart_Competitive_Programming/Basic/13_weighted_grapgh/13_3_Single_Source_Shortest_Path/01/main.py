n = int(input())
adjc_list = [[] for _ in range(n)]
INF = 99999999999999999999
V = [ele for ele in range(n)]
S = []
d = [INF] * n
p = [ele for ele in range(n)]

for i in range(n):
    tmp = [int(ele) for ele in input().split()]
    for j in range(1, tmp[1]*2, 2):
        v = tmp[j+1]
        w = tmp[j+2]
        adjc_list[i].append([w, v])
    adjc_list[i].sort()


def my_dijkstra_solver():
    root = 0  # given
    # 1. 初期化
    d = [INF] * n
    d[root] = 0
    VS = V

    # 2. 以下の処理を、S = Vになるまで繰り返す
    while VS:
        # 2.1. V-S の中から、 d[u] が最小である頂点 u を選択する。
        u = VS[0]
        for i in VS:
            if d[i] < d[u]:
                u = i

        S.append(u)  # 2.2. u を S に追加する.

        # 2.3. u に隣接し, かつ V-S に属するすべての頂点 v に対する以下の値を更新する
        VS.remove(u)
        for w, v in adjc_list[u]:
            if v in VS:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    p[v] = u  # 親をどこかで使うのはわかるが一旦忘れよう

    for i, cost in enumerate(d):
        print(i, cost)


if __name__ == "__main__":
    my_dijkstra_solver()
