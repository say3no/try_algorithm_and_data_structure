# vim: set fileencoding=utf-8:
def main():
    b = [0] * 5
    sim_bin(b, 0, len(b))


def sim_bin(b, i, j):
    #  重複がでてくる。なんでだ？？？？？？？？？？？
    if i + 1 <= j:
        b[i] = 0
        sim_bin(b, i + 1, j)
        b[i] = 1
        sim_bin(b, i + 1, j)


if __name__ == "__main__":
    main()
