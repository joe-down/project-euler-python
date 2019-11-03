def main(maximum_value: int = 2):
    longest_chain: list = [1, 1]
    for n in range(1, maximum_value):
        chain_length: int = 1
        next_value: int = n
        while next_value > 1:
            if next_value % 2 == 0:
                next_value: int = next_value // 2
            else:
                next_value: int = 3 * next_value + 1
            chain_length += 1
        if chain_length > longest_chain[1]:
            longest_chain: list = [n, chain_length]
    print(longest_chain)


main(maximum_value=1000000)
