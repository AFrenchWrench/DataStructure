def build_post_order(in_order, pre_order):
    if not pre_order or not in_order:
        return []

    root = pre_order[0]
    root_index = in_order.index(root)

    left_in_order = in_order[:root_index]
    right_in_order = in_order[root_index + 1 :]

    left_pre_order = pre_order[1 : 1 + len(left_in_order)]
    right_pre_order = pre_order[1 + len(left_in_order) :]

    left_post = build_post_order(left_in_order, left_pre_order)
    right_post = build_post_order(right_in_order, right_pre_order)

    return left_post + right_post + [root]


n = int(input())

in_order = list(input().split())
pre_order = list(input().split())

print(" ".join(build_post_order(in_order, pre_order)))
