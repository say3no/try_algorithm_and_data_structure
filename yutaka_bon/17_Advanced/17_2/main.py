import sys
input = sys.stdin.readline


def main():
    N, W = [int(ele) for ele in input().split()]
    items = [None] * N
    table = [[0] * (W+1) for _ in range(N+1)]
    for idx in range(N):
        v, w = [int(ele) for ele in input().split()]
        items[idx] = Item(v, w)

    for w_i in range(W):
        for i_i in range(N):
            table[w_i][i_i]

    for i in table:
        print(i)


class Item():

    def __init__(self, v, w):
        self.v = v
        self.w = w


if __name__ == "__main__":
    main()
