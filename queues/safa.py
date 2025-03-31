MAXN = 300000 + 1
ps = [0] * MAXN
numbers = [0] * MAXN
pointers = [0] * MAXN
point_to_number = 0

n, q = map(int, input().split())

for _ in range(q):
    t = list(map(int, input().split()))

    if t[0] == 1:
        x = t[1]
        point_to_number += 1
        numbers[point_to_number] = x
        ps[point_to_number] = x + ps[point_to_number - 1]
    else:
        i, j = t[1], t[2]
        print(ps[j + pointers[i]] - ps[pointers[i]])
        pointers[i] += j
