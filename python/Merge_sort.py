import time

def add_list(Llist, Rlist):
    tmp_list = []
    while len(Llist) > 0 and len(Rlist) > 0:
        if Llist[0] <= Rlist[0]:
            tmp_list.append(Llist.pop(0))
        else:
            tmp_list.append(Rlist.pop(0))
    tmp_list += Llist
    tmp_list += Rlist

    return tmp_list

def merge_sort(input_list):
    mid = len(input_list)/2

    if len(input_list) <= 1:
        return input_list
    else:
        left = merge_sort(input_list[:int(mid)])
        right = merge_sort(input_list[int(mid):])
        return add_list(left, right)


if __name__ == "__main__":
    my_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    print(merge_sort(my_list))
    end = time.perf_counter()
    print(end-beg)
    another_list = [1, 2, 6, 4, 10, 7, 4, 23, 9]
    beg = time.perf_counter()
    another_list.sort()
    end = time.perf_counter()
    print(another_list, end-beg)
