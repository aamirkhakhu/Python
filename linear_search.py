def iterative_linear_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

def recursion_linear_search(arr, element, index = 0):
    if arr[index] == element:
        return index
    else:
        return recursion_linear_search(arr, element, index+1)
    pass

def main():
    print 'Main called'
    arr = [11, 22, 33, 44, 55, 66, 77, 88]
    print iterative_linear_search(arr, 22)
    print recursion_linear_search(arr, 33)
    pass


if __name__ == "__main__":
    main()
