# vim: set fileencoding=utf-8 :
pre_order_str = ""
in_order_str = ""
post_order_str = ""


def main():
    n = input()
    nodes = [Node() for _ in xrange(n)]
    for node in nodes:
        node.idx, node.left, node.right = map(int, raw_input().split())
        if 0 < node.left:
            nodes[node.left].parent = node.idx

        if 0 < node.right:
            nodes[node.right].parent = node.idx

    root_idx = [node.idx for node in nodes if node.parent == -1][0]

    print("Preorder")
    pre_order(nodes, root_idx)
    print(pre_order_str)

    print("Ineorder")
    in_order(nodes, root_idx)
    print(in_order_str)

    print("Posteorder")
    post_order(nodes, root_idx)
    print(post_order_str)


def pre_order(nodes, idx):
    global pre_order_str
    pre_order_str += str(nodes[idx].idx) + " "

    if nodes[idx].left != -1:
        pre_order(nodes, nodes[idx].left)

    if nodes[idx].right != -1:
        pre_order(nodes, nodes[idx].right)


def in_order(nodes, idx):
    global in_order_str
    if nodes[idx].left != -1:
        in_order(nodes, nodes[idx].left)

    in_order_str += str(nodes[idx].idx) + " "

    if nodes[idx].right != -1:
        in_order(nodes, nodes[idx].right)


def post_order(nodes, idx):
    global post_order_str
    if nodes[idx].left != -1:
        post_order(nodes, nodes[idx].left)

    if nodes[idx].right != -1:
        post_order(nodes, nodes[idx].right)

    post_order_str += str(nodes[idx].idx) + " "


class Node(object):

    def __init__(self):
        self.idx = None
        self.left = None
        self.right = None
        self.parent = -1

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
