# vim: set fileencoding=utf-8:
import time
import sys
from functools import lru_cache


def main():
    while yet:
        stack = [min(yet)]
        dfs(stack)

    for i, detected_at, finished_at in zip(range(1, n + 1), d, f):
        print(str(i) + " " + str(detected_at) + " " + str(finished_at))


def dfs(stack):
    global yet, ct, graph, d, f
    ct += 1
    d[stack[-1]-1] = ct
    yet.remove(stack[-1])

    for i, adjacency in enumerate(graph[stack[-1]]):
        if adjacency == 1 and i in yet:  # 隣接かつ未探索であれば、stackにpush
            stack.append(i)
            dfs(stack)
    else:
        ct += 1
        f[(stack[-1]-1)] = ct
        stack.pop()


if __name__ == "__main__":
    start = time.time()

    n = int(sys.stdin.readline().rstrip())
    graph = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        tmp = [int(ele) for ele in sys.stdin.readline().rstrip().split()]
        for j in tmp[2:]:
            graph[i][j] = 1

    d = [-1] * (n+1)
    f = [-1] * (n+1)
    yet = [ele for ele in range(1, n+1)]
    ct = 0

    main()
