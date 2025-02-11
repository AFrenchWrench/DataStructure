n, q = map(int, input().split())

active = [1] * n

for _ in range(q):
    operation, idx = map(int, input().split())

    if operation == 1:
        try:
            print(active.index(1, idx) + 1)
        except ValueError:
            print(-1)
    else:
        active[idx - 1] = 0
