# vim: set fileencoding=utf-8:
"""
TEST:
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


def main():
    n = input()
    nodes = [0] * n
    for i in xrange(n):
        a, l, r = map(int, raw_input().split())
        nodes[i] = Node(a, l, r)

    # 子の情報から親を探す
    for i in xrange(n):
        if nodes[i].l != -1:
            nodes[l].p = i
            continue
        elif nodes[i].r != -1:
            nodes[l].p = i
            continue

    # typeを決める。set_type()中で、ついでにrootの親を-1に変更する
    for i in xrange(n):
        nodes[i].set_type()

    # 深さを探す
    for i in xrange(n):
        nodes[i].depth = cal_depth(nodes, i, 0)

    for n in nodes:
        n.show_ans()

    # 高さを探す。高さは、あるノードから到達可能な葉のうち、その距離が最大のもの高さという
    for i in [n.id for n in nodes if n.type == "leaf"]:
        cal_height(nodes, i, 0)


def cal_depth(nodes, i, depth):
    if nodes[i].type != "root":
        return depth

    return cal_depth(nodes, nodes[i].p, depth + 1)


def cal_height(nodes, i, height):
    """
    cal_depthと違って注意が必要なのは、root->leafへと下るように走査していくと、高さが１つ増えるごとに範囲が2倍されるということ。
    なので、逆に、leaf->rootへと駆け上がって行き、すでに値がある場合は、max(already, new)で高さを更新する。
    そうすれば、leafの数の走査で済む。
    """
    print(height)
    print(nodes[i].height)
    if max(height, nodes[i].height) == height:
        nodes[i].height = height
    else:
        return "loose"

    if nodes[i].type == "root":
        return "win"

    return cal_height(nodes, nodes[i].p, height + 1)


class Node(object):
    def __init__(self, uid, l, r):
        self.id = uid
        self.l = l
        self.r = r
        self.chil_num = self.__get_chil_num()
        self.p = None
        self.bros = None
        self.depth = None
        self.height = -1
        self.type = None

    def __get_chil_num(self):
        if self.l == -1 and self.r == -1:
            return 0
        elif self.l == -1 or self.r == -1:
            return 1
        else:
            return 2

    def set_type(self):
        if self.chil_num == 0:
            self.type = "leaf"
        elif self.chil_num != 0 and self.p is not None:
            self.type = "internal node"
        elif self.chil_num != 0 and self.p is None:
            self.type = "root"
            self.p = -1

    def show_ans(self):
        print("node %s: parent = %s, degree = %s, depth = %s, height = %s, %s" % (
            self.id, self.p, self.chil_num, self.depth, self.height, self.type))


if __name__ == "__main__":
    main()
