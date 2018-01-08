# Algorithm to calculate power(k,n)
def power_of(number, power):
    result = 1

    if power == 0:
        return result

    for i in range(power):
        result = result * number
    return result

if __name__ == "__main__":
    print power_of(5, 1)
    print power_of(5, 0)
