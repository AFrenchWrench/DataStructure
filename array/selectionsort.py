n, p = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, p + 1):
    min_index = i - 1
    for j in range(i, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i - 1], arr[min_index] = arr[min_index], arr[i - 1]

print(" ".join(map(str, arr)))
