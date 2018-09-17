# vim: set fileencoding=utf-8 :
pre_order_str = ""
in_order_str = ""


def main():
    m = input()
    cmds = [""] * m
    vals = [0] * m
    for i in xrange(m):
        imp = raw_input()
        if imp == "print":
            cmds[i] = imp
            vals[i] = None
        else:
            cmds[i], val = imp.split()
            vals[i] = int(val)

    root = STNode()
    for cmd, val in zip(cmds, vals):
        if cmd == "insert":
            cmd_insert(root, val)
        elif cmd == "print":
            cmd_print(node=root)


def cmd_insert(root, val):
    """
    1. root nodeから探索を始めて、 new_node の親となるNodeを探す
    """
    p, mes = find_parent(node=root, val=val) # TypeError: root 以外の nodeを参照できず、'NoneType' object is not iterable

    if mes == "root":
        root.val = val
        pass
    elif mes == "left":
        newbie = STNode(parent=p, val=val)
        swap = p.left
        p.left = newbie

        if swap is None:
            pass
        else:
            swap.parent = newbie
            if swap.val <= newbie.val:
                newbie.left = swap
            else:
                newbie.right = swap

    elif mes == "right":
        newbie = STNode(parent=p, val=val)
        swap = p.right
        p.right = newbie

        if swap is None:
            pass
        else:
            swap.parent = newbie
            if swap.val <= newbie.val:
                newbie.left = swap
            else:
                newbie.right = swap


def find_parent(node, val):
    """
    valが与えられる時, nodeを根とした木探索によって、その親となるBSTを返す。
    :param node:
    :param val: val for finding parent and child
    :return: parent, child
    """
    print(val)

    if node.parent is None and node.val is None:  # 一人目, rootが生まれた時のための処理
        node.val = val
        return node, "root"

    elif val <= node.val:  # node.left.valがないときもある
        if node.left is None or node.left.val < val:
            print("%s, hidari da yo~" % node.val)
            return node, "left"
        else:
            find_parent(node.left, val)

    elif node.val < val:  # node.left.valがないときもある
        if node.right is None or val < node.right.val:
            return node, "right"
        else:
            find_parent(node.right, val)


def cmd_print(node):
    global pre_order_str
    global in_order_str
    pre_order_str = ""
    in_order_str = ""

    node.pre_order()
    print(pre_order_str)
    node.in_order()
    print(in_order_str)


class STNode(object):
    def __init__(self, parent=None, left=None, right=None, val=None):
        self.parent = parent
        self.left = left
        self.right = right
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

TEST INPUT:
14
insert 30
print
insert 88
print
insert 12
print
insert 1
print
insert 20
print
insert 17
print
insert 25
print

TEST OUTPUT:
1 12 17 20 25 30 88
30 12 1 20 17 25 88
"""
