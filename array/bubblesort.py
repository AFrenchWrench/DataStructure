n, p = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, p + 1):
    for j in range(n - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
         

print(" ".join(map(str, arr)))