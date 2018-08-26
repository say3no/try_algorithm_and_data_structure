# vim: set fileencoding=utf-8 :
# TODO: あとで二重連鎖木での実装を書き直さないとね。
"""
与えられる情報は、id,子の数、子の番号だけである。
期待した出力は、これに加えて、parent, depth, type。
子だけがはわかるのだから、既知情報でノードを作成したあと、子を持っていないノードからさかのぼっていくことによって、
親が何者であるかが判定できる。
"""


def main():
    n = input()
    ids = [0] * n
    ks = [0] * n
    children = [0] * n
    nodes = [0] * n
    for i in xrange(n):
        given = [ele for ele in raw_input().split()]
        ids[i] = given[0]
        ks[i] = given[1]
        children[i] = map(int, given[2:])

    # とりまid,cを追加
    for i in xrange(n):
        nodes[i] = Node(id=ids[i], c=children[i], k=ks[i])

    # 子供情報から、親を紐付ける
    for i in xrange(n):
        if nodes[i].k > 0:
            for ele in nodes[i].children:
                nodes[ele].set_parent(i)

    # 子、親が出揃ったので、typeを決める
    for i in xrange(n):
        nodes[i].set_type()

    # すべてのノードに対して親子関係がしめされたので、depthを再帰的に計算していく
    for i in xrange(n):
        depth = cal_depth(nodes, i, 0)
        nodes[i].set_depth(depth)

    # 最終出力
    for i in xrange(n):
        nodes[i].show_ans()


def cal_depth(nodes, id, depth):
    if nodes[id].parent == -1:
        return depth

    return cal_depth(nodes, nodes[id].parent, depth + 1)


class Node(object):

    def __init__(self, id, k, c):
        self.id = id
        self.k = k
        self.children = c
        self.parent = "unk"
        self.type = "unk"
        self.depth = "unk"

    def show_ans(self):
        print("node %s: parent = %s , depth = %r, %s, %s" % (self.id, self.parent, self.depth, self.type,
                                                             self.children))

    def set_parent(self, p):
        self.parent = p

    def set_type(self):
        if self.k == 0:
            t = "leaf"
        elif 0 < self.k and self.parent != "unk":
            t = "internal nodes"
        else:
            t = "root"
            self.parent = -1

        self.type = t

    def set_depth(self, d):
        self.depth = d


if __name__ == "__main__":
    main()
