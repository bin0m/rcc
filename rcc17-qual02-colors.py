def getnext(x, k):
    if x < k:
        return x + 1
    else:
        return 1


n, m, k = map(int, input().split())
in_matrix = []
for i in range(0, n):
    line = [int(x) - 1 for x in input().split()]
    in_matrix.append(line)

for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            avl_colors = set(x for x in range(1, n))
            val = 1
            # left exists
            if j > 0 and mat[i][j - 1] > 0:
                avl_colors.discard(mat[i][j - 1])
                val = getnext(mat[i][j - 1], k)
                # left and up exists
                if i > 0 and mat[i - 1][j] > 0:
                    avl_colors.discard(mat[i - 1][j])
                    # up > left
                    if mat[i - 1][j] > mat[i][j - 1]:
                        val = getnext(mat[i - 1][j], k)
            # just up exists
            elif i > 0 and mat[i - 1][j] > 0:
                val = getnext(mat[i - 1][j], k)
                avl_colors.discard(mat[i - 1][j])
            mat[i][j] = val

print(mat)

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
# s = set(x for x in range(1,n))
# print(s.pop())
