def represent_number_in_bits(number):
    str = ""
    while (number > 0):
        if number % 2 == 0:
             str = str + "0"
        else:
            str = str + "1"
        number = number / 2

    return str[::-1]

# Number of bit to be flipped to convert one number to another
def number_to_be_flipped(num1, num2):
    res = num1 ^ num2
    count = 0
    while (res > 0):
        count += res & 1
        res >>= 1
    return count

if __name__ == "__main__":
    print represent_number_in_bits(10)
    print represent_number_in_bits(20)
    res = number_to_be_flipped(10, 20)
    print res