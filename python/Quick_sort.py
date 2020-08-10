import time

def quick_sort(input_list):
    l = len(input_list)
    if l <= 1: return input_list
    if l == 2:
        if input_list[0] > input_list[1]:
            input_list[0], input_list[1] = input_list[1], input_list[0]
        return input_list
    if input_list[-1] < input_list[0] and input_list[-1] < input_list[l//2]:
        if input_list[l//2] < input_list[0]:
            input_list[l//2], input_list[0] = input_list[0], input_list[l//2]
    elif input_list[-1] >= input_list[0] and input_list[-1] >= input_list[l//2]:
        if input_list[l//2] >= input_list[0]:
            input_list[l//2], input_list[0] = input_list[0], input_list[l//2]
    i = j = 0
    mid = input_list[-1]
    while j < l-1:
        if input_list[j] < mid:
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
            j += 1
        else:
            j += 1
    input_list[i], input_list[-1] = input_list[-1], input_list[i]
    return quick_sort(input_list[0:i]) + [mid] + quick_sort(input_list[i+1:])
    


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
            input_list[i], input_list[j] = input_list[j], input_list[i]
            i += 1
            j += 1
        else:
            j += 1
    input_list[i], input_list[j] = input_list[j], input_list[i]
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
