# vim: set fileencoding=utf-8:
def main():
    b = [0] * 4
    sim_bin(b)


def sim_bin(b):
    if i - 1 != len(b):
        sim_bin(b, i)

    b[i] = 1
    print(b)


if __name__ == "__main__":
    main()
