# vim: set fileencoding=utf-8:
import random
import time


def main():
    SIZE = 1000000
    TOP = SIZE * 10
    a = [random.randint(0, TOP) for _ in xrange(SIZE)]
    target = random.randint(0, SIZE - 1)

    liner_search(a[target], a)

    a.sort()

    binary_search(a[target], a)


def liner_search(v, l):
    # 観ての通り、最速でO(1),最悪O(N)となる
    # 良い点は、ソートが不要な点
    for idx, value in enumerate(l):
        if v == value:
            return idx

    return False


def binary_search(v, l):
    # ソート済みであること
    s = 0
    e = len(l) - 1
    m = (len(l) - 1) / 2
    while l[m] != v:
        if len(l[s:e]) == 1:
            return "NOT FOUND"
        if v < l[m]:
            e = m
            m = e / 2
        elif l[m] < v:
            s = m + 1
            m = (s + e) / 2

    return m


if __name__ == "__main__":
    main()
