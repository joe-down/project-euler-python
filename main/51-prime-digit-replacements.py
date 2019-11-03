def find_next_prime(previous_prime: int) -> int:
    for possible_prime in range(previous_prime + 1, 2 * previous_prime):
        possible_prime_status: bool = True
        for possible_factor in range(2, int(possible_prime ** 0.5) + 1):
            if possible_prime % possible_factor == 0:
                possible_prime_status: bool = False
                break
        if possible_prime_status:
            return possible_prime


def check_prime(value: int) -> bool:
    if value < 2:
        return False
    for possible_factor in range(2, int(value ** 0.5) + 1):
        if value % possible_factor == 0:
            return False
    return True


def construct_possible_prime(number_mask: str, current_prime: str, replacement_digit: str) -> int:
    possible_prime: str = ''
    for digit_index, digit in enumerate(number_mask):
        if digit == '0':
            possible_prime += current_prime[digit_index]
        else:
            possible_prime += replacement_digit
    return int(possible_prime)


def main(required_prime_count: int = 1):
    current_prime: int = 2
    prime_found: bool = False
    while not prime_found:
        for number_mask in (('0' * (len(str(current_prime)) - len(bin(binary_value)[2:])) + str(bin(binary_value)[2:]))
                            for binary_value in range(1, 2 ** len(str(current_prime)))):
            prime_family: set = set()
            for replacement_digit in (str(digit) for digit in range(1, 10)):
                possible_prime: int = construct_possible_prime(number_mask, str(current_prime), replacement_digit)
                if check_prime(possible_prime):
                    prime_family.add(possible_prime)
            if len(prime_family) == required_prime_count:
                print(min(prime_family))
                prime_found: bool = True
        current_prime: int = find_next_prime(current_prime)


main(required_prime_count=8)
