current_prime = 999
for number_mask in (('0'*(len(str(current_prime))-len(bin(binary_value)[2:])) + str(bin(binary_value)[2:])) for binary_value in range(1, 2 ** len(str(current_prime)))):
    print(number_mask)