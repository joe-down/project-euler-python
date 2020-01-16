def ceiling(value: float) -> int:
    if value == int(value):
        return int(value)
    return int(value // 1) + 1


def old_p(n: int) -> int:
    if n <= 1:
        return 1
    combination_count: int = 0
    left_pile: int
    for left_pile in range(n, ceiling(n / 2) - 1, -1):
        combination_count += p(n - left_pile)
    left_pile: int
    for left_pile in range(ceiling(n / 2) - 1, 0, -1):
        pass
    return combination_count


def p(n: int) -> int:
    coins: list = n * [1]
    print(coins)
    combination_count: int = 0
    while True:


def main():
    print(p(3))


main()
