n = input()
seq_length = 0

for i in range(1, len(n) ):
    if n[i - 1] == n[i]:
        seq_length += 1
    else:
        if seq_length % 2 == 0:
            break
        else:
            seq_length = 0

if seq_length % 2 == 0:
    print("bad")
else:
    print("khoob")
