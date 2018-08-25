# vim: set fileencoding=utf-8:
def main():
    b = [0] * 10
    sim_bin(b)


def sim_bin(b):
    print(b)
    if len(b) != 1:
        sim_bin(b[1:])


if __name__ == "__main__":
    main()
