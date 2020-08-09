import time
def bubble_sort(list_a):
    l = len(list_a)
    for i in range(l, 0, -1):
        flag = 0
        for j in range(i-1):
            if list_a[j+1] < list_a[j]:
                list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
                flag = 1
        if flag == 0:
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