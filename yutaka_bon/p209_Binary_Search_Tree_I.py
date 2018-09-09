# vim: set fileencoding=utf-8 :
pre_order_str = ""
in_order_str = ""


def main():
    m = input()
    cmds = [""] * m
    vals = [0] * m
    for i in xrange(m):
        cmds[i], val = raw_input().split()
        vals[i] = int(val)

    root = STNode()
    for cmd, val in zip(cmds, vals):
        if cmd == "insert":
            insert_node(root, STNode(val=val))
        elif cmd == "print":
            print_node(root)


def insert_node(node, new_node):
    if node.val:
        if node.left.val < new_node.val <= node.val:  # 左側へ。ただし、node.left.valが存在しない場合もある。


        elif node.left.val < new_node.val <= node.val:  # 右側へ

    else:  # まだひとつも STNode.val がない場合
        node.val = new_node.val
        return


def print_node(node):
    global pre_order_str
    global in_order_str
    pre_order_str = ""
    in_order_str = ""

    node.pre_order()
    print(pre_order_str)
    node.in_order()
    print(in_order_str)


class STNode(object):
    def __init__(self, val=None):
        self.parent = None
        self.left = None
        self.right = None
        self.val = val

    def pre_order(self):
        global pre_order_str
        pre_order_str += str(self.val) + " "
        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        global in_order_str
        if self.left:
            self.left.in_order()

        in_order_str += str(self.val) + " "

        if self.right:
            self.right.in_order()


if __name__ == "__main__":
    main()

"""
TEST INPUT:
8
insert 30
insert 88
insert 12
insert 1
insert 20
insert 17
insert 25
print

TEST OUTPUT:
1 12 17 20 25 30 88
30 12 1 20 17 25 88
"""
