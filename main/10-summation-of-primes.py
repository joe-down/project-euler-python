def find_next_prime(previous_prime: int) -> int:
    for possible_prime in range(previous_prime + 1, 2 * previous_prime):
        possible_prime_status: bool = True
        possible_factor: int = 2
        maximum_possible_factor: int = possible_prime // possible_factor + 1
        while possible_factor < maximum_possible_factor:
            if possible_prime % possible_factor == 0:
                possible_prime_status: bool = False
                break
            possible_factor += 1
            maximum_possible_factor: int = possible_prime // possible_factor + 1
        if possible_prime_status:
            return possible_prime


def find_prime_sum(maximum_value: int) -> int:
    prime_sum: int = 2
    prime: int = find_next_prime(2)
    while prime < maximum_value:
        prime_sum += prime
        prime: int = find_next_prime(prime)
    return prime_sum


def main():
    print(find_prime_sum(2000000))


main()
