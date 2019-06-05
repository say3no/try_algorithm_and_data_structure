V_num, E_num, r = [int(ele) for ele in input().split()]
adjc_list = []
for _ in range(V_num):
    adjc_list.append([])

for _ in range(E_num):
    s, n, w = [int(ele) for ele in input().split()]
    adjc_list[s].append([w, n])


def main():


if __name__ == "__main__":
    main()
