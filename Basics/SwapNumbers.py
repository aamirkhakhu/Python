def swap_numbers_with_temp_var(number1, number2):
    print "====================================================="
    print "Original numbers {0} and {1}".format(number1, number2)
    number1 = number1 + number2
    number2 = number1 - number2
    number1 = number1 - number2
    print "Swapped numbers {0} and {1}".format(number1, number2)
    print "====================================================="

def swap_numbers(number1, number2):
    print "====================================================="
    print "Original numbers {0} and {1}".format(number1, number2)
    temp = number1
    number1 = number2
    number2 = temp
    print "Swapped numbers {0} and {1}".format(number1, number2)
    print "====================================================="

if __name__ == '__main__':
    swap_numbers_with_temp_var(10, 20)
    swap_numbers(10, 20)
