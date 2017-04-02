n = int(input())
powers = [int(x) for x in input().split()]
sums = 0
for x in powers:
    sums += x
half = sums // 2
for i in range(0,n-1):
    if powers[i] == half:
        powers[i], powers[n-1] = powers[n-1], powers[i]
print(powers)