n, p = map(int, input().split())
arr = list(map(int, input().split()))

if n > 1:
    for i in range(1, p + 1):
        current_no = arr[i]
        for j in range(len(arr[:i]) - 1, -1, -1):
            if arr[j] > current_no:
                arr[j], arr[j + 1] = current_no, arr[j]
            else:
                break

print(" ".join(map(str, arr)))
