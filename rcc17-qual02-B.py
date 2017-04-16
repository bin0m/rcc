def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


# start
t = int(input())
for i in range(0, t):
    a, b, c, d = map(int, input().split())
    up = lcm(a, c)
    down = gcd(b, d)
    print(up, down)

