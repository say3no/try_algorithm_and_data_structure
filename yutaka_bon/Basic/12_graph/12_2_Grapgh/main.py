
N = int(input())
T = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    tmp = [int(ele) for ele in input().split()]
    from_ = tmp[0]
    for j in tmp[2:]:
        T[from_][j] = 1


def main():
    for i in T[1:]:
        ans = ""
        for j in i[1:]:
            ans += str(j) + " "
        print(ans[:-1])


if __name__ == "__main__":
    main()
