t = int(input())
for i in range(0, t):
    n, m = map(int, input().split())
    mat = []
    for i in range(0, n):
        row = [None] * m
        mat.append(row)

    person = m * n
    distance = 0
    i = 0
    j = 0
    while person > 0:
        if distance < n:
            i = distance
            j = 0
        else:
            i = n - 1
            j = distance - n + 1
        while j < m and i >= 0:
            mat[i][j] = person
            person -= 1
            i -= 1
            j += 1
        distance += 1

    for i in range(0, n):
        print(*mat[i])
