import itertools


def count_swaps(array):
    n = len(array)
    darr = list(array)
    swaps = 0
    for i in range(0, n):
        next_min = i + 1
        if darr[i] != next_min:
            for j in range(i + 1, n):
                if darr[j] == next_min:
                    darr[i], darr[j] = darr[j], darr[i]
                    swaps += 1
                    break
    return swaps


# start point
n = int("5")
a = [int(x) for x in "0 4 0 2 5".split()]
busy_set = set()
for elem in a:
    if elem != 0:
        busy_set.add(elem)
avlbl_set = set(range(1, n)) - busy_set
perms = list(itertools.permutations(avlbl_set))
max_swaps = 0
curr_swaps = 0
result = []
for perm in perms:
    b = list(a)
    perm_ind = 0
    for ind in range(0, n):
        if a[ind] == 0:
            b[ind] = perm[perm_ind]
            perm_ind += 1
            if perm_ind == len(avlbl_set):
                break
    curr_swaps = count_swaps(b)
    if curr_swaps > max_swaps:
        max_swaps = curr_swaps
        result = b
        if max_swaps == n - 1:
            break
print(max_swaps)
print(result)
