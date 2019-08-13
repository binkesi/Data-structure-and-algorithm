import time

def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = input_list[-1]
        right = []
        for i in input_list:
            if i > mid:
                right.append(input_list.pop(input_list.index(i)))
        input_list.pop(input_list.index(mid))
        left = input_list
        return quick_sort(left) + [mid] + quick_sort(right)


if __name__ == "__main__":
    my_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    print(quick_sort(my_list))
    end = time.perf_counter()
    print(end-beg)
    another_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    another_list.sort()
    end = time.perf_counter()
    print(another_list, end-beg)