# vim: set fileencoding=utf-8 :
pre_order_str = ""


def main():
    n = input()
    nodes = [Node() for _ in xrange(n)]
    for node in nodes:
        idx, left, right = map(int, raw_input().split())
        node.idx = idx
        if 0 < left:
            nodes[left].parent = nodes[node.idx]
            node.left = nodes[left]

        if 0 < right:
            nodes[right].parent = nodes[idx]
            node.right = nodes[right]

    for node in nodes:
        node.show_ans()

    root_idx = [node.idx for node in nodes if node.parent is None][0]
    print("Pre Order")
    pre_order(nodes[root_idx])
    print("In Order")
    in_order(nodes[root_idx])
    print("Post Order")
    post_order(nodes[root_idx])


def pre_order(node):
    print(node.idx)

    if node.left:
        pre_order(node.left)

    if node.right:
        pre_order(node.right)


def in_order(node):
    if node.left:
        in_order(node.left)

    print(node.idx)

    if node.right:
        in_order(node.right)


def post_order(node):
    if node.left:
        post_order(node.left)

    if node.right:
        post_order(node.right)

    print(node.idx)


class Node(object):

    def __init__(self):
        self.idx = None
        self.left = None
        self.right = None
        self.parent = None

    def show_ans(self):
        print("idx: %s, left: %s, right: %s, parent: %s" % (self.idx, self.left, self.right, self.parent))


if __name__ == "__main__":
    main()

""" TEST
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1

"""
