import collections
import sys
sys.setrecursionlimit(100000)

n, m = [int(ele) for ele in input().split()]
graph = [[i] for i in range(n)]
grps = [-1] * n
s = [-1] * (m+1)
t = [-1] * (m+1)

for _ in range(m):
    k, l = [int(ele) for ele in input().split()]
    graph[k].append(l)
    graph[l].append(k)

q = int(input())

s_q = [-1] * (q)
s_t = [-1] * (q)

for i in range(q):
    s_q[i], s_t[i] = [int(ele) for ele in input().split()]


yet = [ele for ele in range(n)]
stack = collections.deque()


def main():
    global graph, grps
    grouping()

    for src, dst in zip(s_q, s_t):
        if grps[src] == grps[dst]:
            print("yes")
        else:
            print("no")


def grouping():
    global yet, stack, grps, tmp
    tmp = 97
    while yet:
        stack.clear()
        stack.appendleft(yet[0])  # 常にmin(yet) = yet[0]
        dfs(stack)
        tmp += 1


def dfs(stack):
    global yet, graph, grps, tmp
    if not stack:
        return

    n = stack[0]
    grps[n] = chr(tmp)
    yet.remove(n)

    for ele in graph[n][1:]:
        if ele in yet:  # 未訪問なら
            stack.appendleft(ele)
            dfs(stack)
    else:
        stack.popleft()


if __name__ == "__main__":
    main()
