queue = []


def push_middle(queue, value):
    if len(queue) == 0:
        queue.append(value)
    else:
        mid_index = (
            (len(queue) - 1) // 2 + 1 if len(queue) % 2 == 0 else len(queue) // 2
        )
        queue.insert(mid_index, value)


def pop_front(queue):
    return -1 if len(queue) == 0 else queue.pop(0)


def pop_middle(queue):
    if len(queue) == 0:
        return -1
    mid_index = (len(queue) - 1) // 2 if len(queue) % 2 != 0 else (len(queue) - 1) // 2
    return queue.pop(mid_index)


def pop_back(queue):
    return -1 if len(queue) == 0 else queue.pop()


n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "PushFront":
        queue.insert(0, command[1])
    elif command[0] == "PushMiddle":
        push_middle(queue, command[1])
    elif command[0] == "PushBack":
        queue.append(command[1])
    elif command[0] == "PopFront":
        pop_front(queue)
    elif command[0] == "PopMiddle":
        pop_middle(queue)
    elif command[0] == "PopBack":
        pop_back(queue)

if queue:
    print(" ".join(queue))
else:
    print("-1")
