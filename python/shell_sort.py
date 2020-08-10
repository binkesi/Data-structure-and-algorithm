def shell_sort(list):
    l = len(list)
    step = l // 2
    while step >= 1:
        for i in range(step, l):
            tmp = list[i]
            j = i
            while j >= 0 and j-step >= 0 and list[j-step] > tmp:
                list[j] = list[j-step]
                j -= step
            list[j] = tmp
        step = step // 2
    return list
    
if __name__ == "__main__":
    list_a = [5, 3, 7, 9, 10, -1, -9, 2]
    print(shell_sort(list_a))