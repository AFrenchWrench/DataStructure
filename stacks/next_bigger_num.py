n = int(input())
numbers = list(map(int, input().split()))

answers = [-1] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= numbers[i]:
        stack.pop()
    if stack:
        answers[i] = stack[-1]
    stack.append(numbers[i])

print(" ".join(map(str, answers)))
