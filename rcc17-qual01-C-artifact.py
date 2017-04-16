import itertools

# start
t = int(input())
for tnum in range(0, t):
    n = int(input())
    alist = []
    blist = []
    xlist = []

    for i in range(n):
        a, b, x = map(int, input().split())
        alist.append(a)
        blist.append(b)
        xlist.append(x)

    best_time = 5000000

    for variant in itertools.permutations(range(n)):
        variant_time = 0
        for k in range(n):
            ktime = 0
            for i in range(n):
                if i <= k:
                    ktime += alist[variant[i]]
                else:
                    ktime += blist[variant[i]]
            ktime *= xlist[variant[k]] * 10 ** -7
            variant_time += ktime
        best_time = min(best_time, variant_time)
    print(best_time)
