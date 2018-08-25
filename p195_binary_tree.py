# vim: set fileencoding=utf-8:
n = input()
id = [999] * n
left = [999] * n
right = [999] * n


for i in xrange(n):
    id[i], left[i], right[i] = map(int, raw_input().split())


def main():
    """ Create Binary Tree"""
    for i in xrange(n):




class BTNode(object):
    def __init__(self, l, r, p):
        self.l = l
        self.r = r
        self.p = p


if __name__ == "__main__":
    main()
