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
        cal(bins, 0, len(bins), m, A)


def cal(b, i, j, m, A):
    if m == cal_sum(b, A):
        print("yes")
        return
    elif i + 1 <= j:
        b[i] = 0
        cal(b, i + 1, j, m, A)
        b[i] = 1
        cal(b, i + 1, j, m, A)


def cal_sum(bins, A):
    ans = 0
    for b, a in zip(bins, A):
        ans += b * a

    return ans


if __name__ == "__main__":
    main()
