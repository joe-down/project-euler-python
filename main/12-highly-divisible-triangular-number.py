class TriangleNumber:
    def __init__(self, length: int):
        self.value: int = 0
        self.triangle_number_number: int = 0
        for i in range(0, length):
            self.add_next_value()

    def add_next_value(self):
        self.triangle_number_number += 1
        self.value += self.triangle_number_number

    def get_divisor_count(self) -> int:
        return len(self.get_divisors())

    def get_divisors(self) -> list:
        divisors: list = []
        for possible_factor in range(1, int(self.value ** 0.5) + 1):
            if self.value % possible_factor == 0:
                divisors.append(possible_factor)
                multiplier: int = self.value // possible_factor
                if multiplier != possible_factor:
                    divisors.append(multiplier)
        return divisors


def main(minimum_divisors: int = 0):
    value_found: bool = False
    triangle_number: TriangleNumber = TriangleNumber(1)
    while not value_found:
        if triangle_number.get_divisor_count() > minimum_divisors:
            break
        triangle_number.add_next_value()
    print(triangle_number.value)


main(minimum_divisors=500)
