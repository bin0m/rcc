import fileinput

for line in fileinput.input():
    name = line.strip()
    print(name)

a = fileinput.input()
b = fileinput.filename()

n, k = map(int, "3 4")

seats = [[False for x in range(2)] for y in range(n)]

reds = list()
blues = list()

for i in range(1, k + 1):
    x, y = map(int, fileinput.input().readline().split())
    x -= 1
    y -= 1
    for j in range(0, n):
        if seats[j][0] is False and seats[j][1] is False:
            if x == j and y == 0:
                reds.append(i)
            elif x == j and y == 1:
                blues.append(i)
            break

        if seats[j][0] is False and seats[j][1] is True:
            if x == j and y == 0:
                reds.append(i)
                blues.append(i)
                break

        if seats[j][0] is True and seats[j][1] is False:
            if x == j and y == 1:
                reds.append(i)
                blues.append(i)
                break
    seats[x][y] = True

print(len(reds), *reds)
print(len(blues), *blues)
