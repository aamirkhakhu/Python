import sys

def iterative_binary_search(arr, element, low, high):
    while (high >= low):
        mid = (low + high) / 2
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def recursive_binary_search(arr, element, low, high):
    if(high >= low):
        mid = (low + high) / 2
        if element == arr[mid]:
            return mid
        elif element < arr[mid]:
            return recursive_binary_search(arr, element, low, mid - 1)
        else:
            return recursive_binary_search(arr, element, mid + 1, high)
    else:
        return -1
    pass

def main():
    arr = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    element = 55
    # if sys.argv[1] is not None:
        # element = int(sys.argv[1])
    # iterative_binary_search(arr, element, low, high)
    print iterative_binary_search(arr, element, 0, len(arr) - 1)

    print recursive_binary_search(arr, element, 0, len(arr) -  1)

    pass

if __name__ == "__main__":
    main()
