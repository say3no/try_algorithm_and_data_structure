# vim: set fileencoding=utf-8 :


def main():
    n = input()
    nodes = [Node(idx=i) for i in xrange(n)]
    pre_order = [int(ele) - 1 for ele in raw_input().split()]
    in_order = [int(ele) - 1 for ele in raw_input().split()]
    post_order = [0] * n

    dive_left(nodes, pre_order, in_order, st=pre_order[0], en=in_order[0])


def dive_left(nodes, pre_order, in_order, st, en):
    idx = pre_order.index(en)
    for i in pre_order[st:idx-1]:
        nodes[i].left = nodes[pre_order[st + i + 1]]


class Node(object):
    def __init__(self, idx):
        self.idx = idx
        self.l = None
        self.r = None
        self.p = None


if __name__ == "__main__":
    main()

"""
TEST:
5
1 2 3 4 5
3 2 4 1 5

Ans:
3 4 2 5 1
"""
