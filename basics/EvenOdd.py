# verify of the number is even or odd

def verify_number_even_odd(number):
    if number % 2 == 0:
        print "Number {0} is Even".format(number)
    else:
        print "Number {0} is odd".format(number)
    pass

print "This line executed"

if __name__ == "__main__":
    print __name__
    number = 10
    verify_number_even_odd(number)
else:
    print "Imported in another module"