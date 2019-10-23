def find_next_prime(previous_prime: int) -> int:
    for possible_prime in range(previous_prime + 1, 2 * previous_prime):
        possible_prime_status: bool = True
        for possible_factor in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % possible_factor == 0:
                possible_prime_status: bool = False
                break
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
