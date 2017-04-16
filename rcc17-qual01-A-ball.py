n = int(input())

for i in range(0, n):
    k, x, y = map(int, input().split())
    turns = 0
    if x == y:
        if k - 1 > x:
            turns = k - x
        else:
            turns = 2
    elif x > y:
        if k > x:
            turns = k - x
        else:
            if x - 1 > y:
                turns = 0
            else:
                turns = 1
    else:
        if k > y:
            turns = k - y
        else:
            if y - 1 > x:
                turns = 0
            else:
                turns = 1
    print(turns)
