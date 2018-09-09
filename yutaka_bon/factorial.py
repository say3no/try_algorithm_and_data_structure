# vim: set fileencoding=utf-8:


def main():
    combs = [comb(20, i) for i in range(1, 21)]
    print(combs)
    print(len(combs))
    print(sum(combs))


def comb(x, y):
    return factorial(x) / (factorial(y) * factorial(x - y))


def factorial(a):
    ans = 1
    for ele in range(1, a + 1):
        ans *= ele

    return ans


if __name__ == "__main__":
    main()
