import time

def binary_search_first(input_list, value):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = low + ((high - low)>>1)
        if input_list[mid] == value:
            while input_list[mid] == value:
                mid = mid - 1
            return mid + 1
        elif input_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_last(input_list, value):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = low + ((high - low)>>1)
        if input_list[mid] == value:
            while input_list[mid] == value:
                mid = mid + 1
            return mid - 1
        elif input_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_high(input_list, value):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = low + ((high - low)>>1)
        if input_list[mid] == value:
            return mid
        elif input_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return high + 1

def binary_search_low(input_list, value):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = low + ((high - low)>>1)
        if input_list[mid] == value:
            while input_list[mid] == value:
                mid = mid + 1
            return mid - 1
        elif input_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1

if __name__ == "__main__":
    my_list = [1, 1, 1, 4, 4, 5, 6, 8, 9, 9, 9, 9, 12, 14, 15, 15, 15, 18, 19, 19, 20]
    print(binary_search_first(my_list, 9))
    print(binary_search_last(my_list, 9))
    print(binary_search_high(my_list, 11))
    print(binary_search_low(my_list, 13))
