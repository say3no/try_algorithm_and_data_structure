# vim: set fileencoding=utf-8:


def main():
    n = input()
    A = [int(ele) for ele in raw_input().split()]
    q = input()
    M = [int(ele) for ele in raw_input().split()]

    A.sort()  # Nは最大で20、組み合わせは 1048,575。qは最大で200だから、 200 * 1,048,575。
    for m in M:
        bins = [1] * len(A)  # 組み合わせをマッピングするバイナリベクタを用意する。
        s = sum(A)
        '''
        全探査をする、という発想に立つからには、というかそうでなくても、探査をする場合は、
        その範囲について自覚しておくべきだ。この場合は、「組み合わせが存在するかどうか」を問う問題であるから、
        pow(2, len(A))通りの組み合わせ基本的にはすべて探査する、という意味合いになる。あとは、それをどのように実装していくかである。
        '''
        if m > s:  # まず、m がsum(A)を超えている場合は、探査の必要がない。
            print("no")
            continue

        # b[i]を0にした時の値が、mと一致したかどうかを表現するプログラム


def cal_bin(i, b):
    # [0,0,0], [0,0,1]
    cal_bin(i, b)


if __name__ == "__main__":
    main()
