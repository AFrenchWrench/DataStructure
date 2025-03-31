class Block:
    def __init__(self, color, start, end, size):
        self.color = color
        self.start = start
        self.end = end
        self.size = size


def solve_balloons(n, balloons):
    result = [-1] * n

    blocks = []
    start = 0
    curr_color = balloons[0]
    for i in range(1, n):
        if balloons[i] != curr_color:
            blocks.append(Block(curr_color, start, i - 1, (i - 1) - start + 1))
            curr_color = balloons[i]
            start = i
    blocks.append(Block(curr_color, start, n - 1, (n - 1) - start + 1))

    day = 1
    while True:
        to_pop = [b for b in blocks if b.size >= 3]

        if not to_pop:
            break

        to_pop.sort(key=lambda b: b.start, reverse=True)

        for block in to_pop:
            for idx in range(block.start, block.end + 1):
                if result[idx] == -1:
                    result[idx] = day

        blocks = [b for b in blocks if b.size < 3]

        merged_blocks = []
        for block in blocks:
            if merged_blocks and merged_blocks[-1].color == block.color:
                merged_blocks[-1].end = block.end
                merged_blocks[-1].size += block.size
            else:
                merged_blocks.append(block)
        blocks = merged_blocks

        day += 1

    return result


n = int(input())
balloons = list(map(int, input().split()))
result = solve_balloons(n, balloons)
print(" ".join(map(str, result)))
