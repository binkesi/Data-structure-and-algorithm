import time


def binary_search(input_list, value):
    l = len(input_list)
    low = 0
    high = l-1
    while low <= high:
        mid = int(low + ((high - low) >> 1))
        if input_list[mid] == value:
            return mid
        elif input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
    return -1

def binary_search_first(input_list, value):
    l = len(input_list)
    low = 0
    high = l-1
    while low <= high:
        mid = int(low + ((high - low) >> 1))
        if input_list[mid] == value:
            while mid-1 >= 0 and input_list[mid-1] == value:
                mid = mid - 1
            return mid
        elif input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
    return -1

def binary_search_last(input_list, value):
    l = len(input_list)
    low = 0
    high = l-1
    while low <= high:
        mid = int(low + ((high - low) >> 1))
        if input_list[mid] == value:
            while mid <= l-1 and input_list[mid] == value:
                mid = mid + 1
            return mid - 1
        elif input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
    return -1

def binary_search_first_bigger(input_list, value):
    l = len(input_list)
    low = 0
    high = l-1
    while low <= high:
        mid = int(low + ((high - low) >> 1))
        if input_list[mid] >= value and input_list[mid-1] < value:
            return mid
        elif input_list[mid] >= value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
    return -1

def binary_search_last_smaller(input_list, value):
    l = len(input_list)
    low = 0
    high = l-1
    while low <= high:
        mid = int(low + ((high - low) >> 1))
        if input_list[mid] <= value and input_list[mid+1] > value:
            return mid
        elif input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] <= value:
            low = mid + 1
    return -1


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 8, 10, 14, 16, 17, 35, 35, 35, 35, 41, 43, 44, 50]
    print(binary_search(my_list, 9))
    print(binary_search_first(my_list, 9))
    print(binary_search_first_bigger(my_list, 89))
    print(binary_search_last_smaller(my_list, -1))
