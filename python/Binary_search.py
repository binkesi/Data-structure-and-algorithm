import time


def binary_search(input_list, value):
    high = len(input_list) - 1
    low = 0
    while low <= high:
        mid = low + ((high - low) >> 1)
        if input_list[mid] == value:
            return mid
        elif input_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 8, 10, 14, 16, 17, 23, 34, 35, 37, 41, 43, 44, 50]
    beg = time.perf_counter()
    print(binary_search(my_list, 35))
    end = time.perf_counter()
    print(end-beg)
