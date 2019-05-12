import sys
input = sys.stdin.readline


# dp
def main():


class Item():
    def __init__(self, v, w):
        self.v = v
        self.w = w


if __name__ == "__main__":
    n = 4
    W = 5
    w = [2, 1, 3, 2]
    v = [3, 2, 4, 2]
    items = [Item(v, w) for v, w in zip(v, w)]
    dp = [[[None] * (n+1)] for _ in range(W+1)]
    main()
