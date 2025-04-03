stack = []

length = input()
s = input()

for c in s:
    if stack and c == stack[-1]:
        stack.pop()
    else:
        stack.append(c)

print("".join(stack))
