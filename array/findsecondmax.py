n = int(input())
arr = list(map(int, input().split()))

# Step 1: Initialize each element as a tuple (value, defeated_list)
players = [(num, []) for num in arr]

# Step 2: Tournament rounds
while len(players) > 1:
    next_round = []
    # Compare elements in pairs
    for i in range(0, len(players) - 1, 2):
        a, defeated_a = players[i]
        b, defeated_b = players[i + 1]

        # Winner and loser
        if a > b:
            next_round.append((a, defeated_a + [b]))
        else:
            next_round.append((b, defeated_b + [a]))

    # If there's an odd element left, it advances automatically
    if len(players) % 2 == 1:
        next_round.append(players[-1])

    players = next_round

# Step 3: Find the second maximum
max_number, defeated_list = players[0]
second_max = defeated_list[0]

for num in defeated_list[1:]:
    if num > second_max:
        second_max = num

# Output
print(max_number, second_max)
