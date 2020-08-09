import time

def insertion_sort(input_list):
    assert isinstance(input_list, list)
    if len(input_list) <= 1:
        return input_list
    for i in range(1, len(input_list)):
        value = input_list[i]
        index = 0
        for j in range(i-1, 0, -1):
            if input_list[j] > value:
                input_list[j+1] = input_list[j]
            else:
                index = j
                break
        input_list[index+1] = value


if __name__ == "__main__":
    my_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    insertion_sort(my_list)
    end = time.perf_counter()
    print(my_list, end-beg)
    another_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    another_list.sort()
    end = time.perf_counter()
    print(another_list, end-beg)

