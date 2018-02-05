# Armstrong
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
def power(number, power):
    result = 1
    if power == 0:
        return result
    for i in range(power):
        result = result * number
    return result

def order(number):
    count = 0
    while number != 0:
        count += 1
        number = number / 10
    return count

def armstrong_number(number):
    actual_number = number
    len = order(number)
    value = 0
    while number != 0:
        temp = number % 10
        value = value + power(temp, len)
        number = number / 10

    if actual_number == value:
        return True
    else:
        return False

if __name__ == "__main__":
    # print order(153)
    print armstrong_number(153)