INF = 99999999999999999999999999
n = int(input())
graph = [[-1] * (n+1) for _ in range(n+1)]
mst = [[-1] * (n+1) for _ in range(n+1)]
V = [ele for ele in range(1, n+1)]
T = []

for i in range(1, n + 1):
    tmp = [int(ele) for ele in input().split()]
    graph[i][1:] = tmp


def my_mst_solver():
    # あるノード n の辺の集合から、もっとも軽いもののindexを知りたい
    # sortされていればすぐだが、graphは添字と依存しているため、sortはできない
    # なので、(w,to) という形で表現された辺のリストがあると非常に便利になるのではないか。
    # これって隣接リストの拡張か？？まあいいや
    ans = 0
    edges = [[0]]
    for i in range(1, n + 1):
        tmp = []
        for to, w in enumerate(graph[i][1:], 1):
            if w != -1:
                tmp.append([w, to])
        tmp.sort()  # pythonのlist.sort()は安定ソートかつ、要素が配列の場合はele[0]でソートする
        edges.append(tmp)

    # 1. Gから任意の頂点 r を選び、それをMSTのルートとしてTに追加する
    root = 1
    T.append(root)
    # 2. 次の処理を T = V になるまで繰り返します。
    # Tに属する頂点と　V - T に属する頂点をつなぐ辺の中で、重みが最小のものである辺 (p_u, u) を選び、
    # それを MST の辺とし、 u を T に追加します

    while set(T) != set(V):
        tmp = [INF, INF]
        for i in T:
            if edges[i] != [] and edges[i][0] < tmp:
                tmp = edges[i][0]
                idx = i
        else:
            # T, MSTの更新
            ans += tmp[0]
            T.append(tmp[1])
            mst[idx][tmp[1]] = tmp[0]
            mst[tmp[1]][idx] = tmp[0]
            # edgesの更新
            for k in range(1, n + 1):
                edges[k] = list(filter(lambda x: x[1] not in T, edges[k]))

    print(ans)


if __name__ == "__main__":
    my_mst_solver()
