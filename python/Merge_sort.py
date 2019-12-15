def merge_sort(input_list):
    if not isinstance(input_list, list):
        raise TypeError("should input a list.")
    length = len(input_list)
    if length == 1:
        return input_list
    else:
        div = int(length/2)
        return merge(merge_sort(input_list[0:div]), merge_sort(input_list[div:length]))


def merge(list1, list2):
    add_list = []
    cur1 = cur2 = 0
    list1.append(None)
    list2.append(None)
    while list1[cur1] is not None and list2[cur2] is not None:
        if list1[cur1] <= list2[cur2]:
            add_list.append(list1[cur1])
            cur1 += 1
            continue
        else:
            add_list.append(list2[cur2])
            cur2 += 1
            continue
    if list1[cur1] is None:
        add_list = add_list + list2[cur2:-1]
    else:
        add_list = add_list + list1[cur1:-1]

    return add_list


if __name__ == "__main__":
    a = [5, 8, 2, 14, 1, 5, 4, 3]
    print(merge_sort(a))

