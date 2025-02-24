n = int(input())

stones = list(map(int, input().split()))

while stones:
    print(
        stones.pop(len(stones) // 2 if len(stones) % 2 != 0 else (len(stones) - 1) // 2),
        end=" ",
    )
