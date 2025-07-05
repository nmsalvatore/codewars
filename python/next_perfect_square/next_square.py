def find_next_square(num: int) -> int:
    root = int(num ** 0.5)

    if root ** 2 != num:
        return -1

    return (root + 1) ** 2
