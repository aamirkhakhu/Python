# factorial of a number
def factorial(number):
    result = 1
    while(number >= 1):
        result = result * number
        number -= 1
    print result

if __name__ == "__main__":
    number = 5
    factorial(number)