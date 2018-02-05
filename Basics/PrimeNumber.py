# check if a number is prime or not
def prime_number(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Geth the prime numbers with the given range
def prime_numbers_within_range(start, end):
    list = []
    for i in range(start, end + 1):
        if(prime_number(i)):
            list.append(i)
    print list

if __name__ == "__main__":
    print(prime_number(13))
    print(prime_number(20))
    print(prime_number(27))
    prime_numbers_within_range(0, 20)
