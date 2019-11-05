def generate_primitive_triple_lengths(maximum_length: int) -> list:
    # Using Euclid's formula
    triples: list = []
    m: int
    for m in range(2, int((maximum_length / 2) ** 0.5) + 1):
        n: int
        for n in range(1, m):
            # m and n must be coprime and cannot both be even
            if ((m + n) % 2 == 1) and check_coprime(m, n):
                a: int = m ** 2 - n ** 2
                b: int = 2 * m * n
                c: int = m ** 2 + n ** 2
                triples.append(a + b + c)
    return triples


def gcd(initial_smaller, initial_larger) -> int:
    # Using Euclid's method
    while initial_larger != 0:
        initial_smaller, initial_larger = initial_larger, initial_smaller % initial_larger
    return initial_smaller


def check_coprime(initial_smaller, initial_larger) -> bool:
    return gcd(initial_smaller, initial_larger) == 1


def main(maximum_length: int = 12):
    primitive_triple_lengths: list = generate_primitive_triple_lengths(maximum_length)
    triple_length_counts: dict = {}
    primitive_triple_length: int
    for primitive_triple_length in primitive_triple_lengths:
        triple_length: int
        for triple_length in range(primitive_triple_length, maximum_length + 1, primitive_triple_length):
            try:
                triple_length_counts[triple_length] += 1
            except KeyError:
                triple_length_counts[triple_length]: int = 1
    print(sum([triple_length_counts[length] == 1 for length in triple_length_counts.keys()]))


main(maximum_length=1500000)
