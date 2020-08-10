def choice_sort(list_a):
    l = len(list_a) 
    if l <= 1:
        return
    for i in range(l):
        min_num = list_a[i]
        index = i
        for j in range(i, l):
            if list_a[j] < min_num:
                min_num = list_a[j]
                index = j
        list_a[i], list_a[index] = list_a[index], list_a[i]
        
if __name__ == "__main__":
    list_a = [5, 3, 7, 9, 10, -1, -9, 2]
    choice_sort(list_a)
    print(list_a)