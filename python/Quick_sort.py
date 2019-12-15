import time

def swap(input_list, i, j):
    tmp = input_list[i]
    input_list[i] = input_list[j]
    input_list[j] = tmp

def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    q_div = input_list[-1]
    i = j = 0
    while j != len(input_list)-1:
        if input_list[j] < q_div:
            swap(input_list, i, j)
            i += 1
            j += 1
        else:
            j += 1
    swap(input_list, i, j)
    left_list = input_list[0:i]
    right_list = input_list[i+1:]
    return(quick_sort(left_list) + [q_div] + quick_sort(right_list))

def find_kth(input_list, k):
    l = len(input_list)
    if k > l:
        return None
    if k == l:
        tmp = input_list[0]
        for i in input_list:
            if i >= tmp:
                tmp = i
        return tmp
    q_div = input_list[-1]
    i = j = 0
    while j != len(input_list)-1:
        if input_list[j] < q_div:
            swap(input_list, i, j)
            i += 1
            j += 1
        else:
            j += 1
    swap(input_list, i, j)
    left_list = input_list[0:i]
    right_list = input_list[i+1:]
    if len(left_list) == k-1:
        return q_div
    elif len(left_list) < k-1:
        return find_kth(right_list, k-1-len(left_list))
    elif len(left_list) > k-1:
        return find_kth(left_list, k)

if __name__ == "__main__":
    my_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    print(quick_sort(my_list))
    end = time.perf_counter()
    print(end-beg)
    beg = time.perf_counter()
    print(find_kth(my_list, 6))
    end = time.perf_counter()
    print(end-beg)
