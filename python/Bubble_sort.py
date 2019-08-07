import time
def bubble_sort(input_list):
    assert isinstance(input_list, list)
    for j in range(0, len(input_list)):
        flag = False
        for i in range(0, len(input_list)-1-j):
            if input_list[i] > input_list[i+1]:
                tmp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = tmp
                flag = True
            else:
                pass
        if flag == False:
            break

if __name__ == "__main__":
    my_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    bubble_sort(my_list)
    end = time.perf_counter()
    print(my_list, end-beg)
    another_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    another_list.sort()
    end = time.perf_counter()
    print(another_list, end-beg)