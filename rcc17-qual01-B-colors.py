# help function to get next color number
def getnext(x, K):
    if x < K:
        return x + 1
    else:
        return 1


# start
t = int(input())
for tnum in range(0, t):
    n, m, k = map(int, input().split())
    mat = []
    for i in range(0, n):
        line = [int(x) - 1 for x in input().split()]
        mat.append(line)

    for i in range(n):
        counter = i % k + 1
        for j in range(m):
            if mat[i][j] == 0:
                mat[i][j] = counter
            counter = getnext(counter, k)

    ans = "YES"

    for i in range(n):
        avl_colors = set(x for x in range(1, k + 1))
        for j in range(m):
            if mat[i][j] == -1:
                mat[i][j] = 0
                avl_colors = set(x for x in range(1, k + 1))
            else:
                if mat[i][j] in avl_colors:
                    avl_colors.remove(mat[i][j])
                else:
                    ans = "NO"
                    break

    for j in range(m):
        avl_colors = set(x for x in range(1, k + 1))
        for i in range(n):
            if mat[i][j] == 0:
                avl_colors = set(x for x in range(1, k + 1))
            else:
                if mat[i][j] in avl_colors:
                    avl_colors.remove(mat[i][j])
                else:
                    ans = "NO"
                    break

    if ans == "YES":
        print(ans)
        for i in range(0, n):
            print(*mat[i])
    else:
        print("NO")

        # for i in range(0, n):
        #     print(*mat[i])
