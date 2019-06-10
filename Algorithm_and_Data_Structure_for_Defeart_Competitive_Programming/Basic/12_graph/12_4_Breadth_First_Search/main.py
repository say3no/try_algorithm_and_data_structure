# vim: set fileencoding=utf-8:
import sys
import collections
INF = 10000000
queue = collections.deque()  # appendleft(), pop()
n = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
yet = [i for i in range(1, n+1)]
ans = [-1] * (n+1)
for i in range(1, n+1):
    tmp = [int(ele) for ele in input().split()]
    for adjc in tmp[2:]:
        graph[i][adjc] = 1

d = [INF] * (n+1)
d[1] = 0

# BFS


def main():
    global queue, d
    queue.appendleft(1)
    bfs(queue)
    d = list(map(lambda x: -1 if x == INF else x, d))
    for i in range(1, n+1):
        print(str(i) + " " + str(d[i]))


def bfs(queue):
    global graph, yet
    if len(queue) == 0:
        return

    n = queue[-1]
    yet.remove(n)

    # 各ノードとの隣接状態をみていく
    for i, adjacency in enumerate(graph[n]):
        if adjacency == 1 and i in yet and i not in queue:  # 隣接 かつ 未探索 かつ queueにもない 待ち行列に加える
            queue.appendleft(i)
            # 隣接していれば、自分自身までの最短コストに1を加えたものとの min() を計算する
            d[i] = min(d[i], d[n] + 1)
    else:
        queue.pop()
        bfs(queue)


if __name__ == "__main__":
    main()
