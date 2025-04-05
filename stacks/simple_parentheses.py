stack = []
open_pairs = []
closed_pairs = []

n = int(input())
parentheses = list(input())

if n % 2 != 0:
    print("not valid")
elif parentheses[0] == ")" or parentheses[-1] == "(":
    print("not valid")
else:
    for i, p in enumerate(parentheses):
        if len(closed_pairs) == n / 2:
            break
        if stack and p != stack[-1]:
            stack.pop()
            closed_pairs.append((open_pairs.pop() + 1, i + 1))
        else:
            stack.append(p)
            open_pairs.append(i)

    if stack:
        print("not valid")
    else:
        print("valid")
        for pair in sorted(closed_pairs, key=lambda x: x[0]):
            print(" ".join(map(str, pair)))
