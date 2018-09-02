# vim: set fileencoding=utf-8 :
pre_order_str = ""
in_order_str = ""
post_order_str = ""


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

    root_idx = [node.idx for node in nodes if node.parent is None][0]
    nodes[root_idx].pre_order()
    nodes[root_idx].in_order()
    nodes[root_idx].post_order()
    print("Pre Oreder")
    print(pre_order_str)
    print("In Oreder")
    print(in_order_str)
    print("Post Oreder")
    print(post_order_str)


class Node(object):

    def __init__(self):
        self.idx = None
        self.left = None
        self.right = None
        self.parent = None

    def pre_order(self):
        global pre_order_str
        pre_order_str += str(self.idx) + " "
        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        global in_order_str

        if self.left:
            self.left.in_order()

        in_order_str += str(self.idx) + " "

        if self.right:
            self.right.in_order()

    def post_order(self):
        global post_order_str
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        post_order_str += str(self.idx) + " "

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
