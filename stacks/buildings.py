n = int(input())
heights = list(map(int, input().split()))

extended = heights + [0]

stack: list[int] = []
max_area = 0

for i, h in enumerate(extended):
    while stack and extended[stack[-1]] > h:
        top = stack.pop()
        height = extended[top]
        left = stack[-1] if stack else -1
        width = i - left - 1
        area = height * width
        if area > max_area:
            max_area = area
    stack.append(i)

print(max_area)
