n = int(input())
seq = input()

stack = []

for c in seq:
    if c == "[" or c == "]":
        if stack and c == "]" and stack[-1] == "[":
            stack.pop()
        else:
            stack.append(c)
    elif c == "(" or c == ")":
        if stack and c == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(c)
    else:
        if stack and c == "}" and stack[-1] == "{":
            stack.pop()
        else:
            stack.append(c)


if stack:
    print("not valid")
else:
    print("valid")
