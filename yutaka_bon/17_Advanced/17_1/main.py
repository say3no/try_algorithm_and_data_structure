import sys
import math
input = sys.stdin.readline

# Coin問題。O(nm)で解ける


def main():
    C, T = init()


def init():
    n, m = [int(ele) for ele in input().split()]
    n += 1
    C = [int(ele) for ele in input().split()]
    T = [[None] * (n) for _ in range(m)]

    for price in range(n):
        for cidx in range(m):
            if price == 0:
                T[price][cidx] == 0
                continue
            else:
                T[price][cidx] == T[price][cidx-1]

    return C, T


if __name__ == "__main__":
    main()
