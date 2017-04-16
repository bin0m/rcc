def generate_binary():
    a, b, c, d = map(int, input().split())
    result = list()
    diff = abs(c - b)
    if diff > 1 or b == c == 0:
        return 'impossible'
    elif diff == 0:
        result.append('0' * (a + 1))
        result.append('1' * d)
        result.append('10' * c)
        return ''.join(result)
    else:
        if c > b:
            result.append('1' * (d + 1))
            result.append('0' * (a + 1))
            result.append('10' * (c - 1))
            return ''.join(result)
        else:
            result.append('0' * (a + 1))
            result.append('1' * (d + 1))
            result.append('01' * (c - 1))
            return ''.join(result)


# start point
n = int(input())
for i in range(0, n):
    print(generate_binary())
