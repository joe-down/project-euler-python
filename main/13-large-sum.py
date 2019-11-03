def main(filename: str = 'numbers.txt'):
    print(sum(int(number.rstrip()) for number in open(filename, 'r')))


main(filename='13-large-sum.txt')
