# arr [0, 1, ... 9]
arr = [num for num in range(10)]
print arr

# using list comprhension with a function
def double(x):
    return x * 2

double_arr = [double(num) for num in range(10) if num % 2 == 0]
print double_arr

# adding more arguments with list comprehension
sum = [x + y for x in [10, 20, 30] for y in [40, 50, 60]]
print sum

