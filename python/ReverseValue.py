# calculate reverse value when merge two ordered list
def merge_value(lis_a, lis_b, sum=0):
    tmp = []
    tag = 0
    index_a = index_b = 0
    while lis_a or lis_b:
        if index_a == len(lis_a):
            tmp += lis_b[index_b:]
            break
        elif index_b == len(lis_b):
            tmp += lis_a[index_a:]
            break

        if lis_a[index_a] <= lis_b[index_b]:
            tmp.append(lis_a[index_a])
            index_a += 1
            tag = 0
        else:
            tmp.append(lis_b[index_b])
            if tag == 0:
                sum = sum + index_b + 1
            else:
                sum += 1
            index_b += 1
    return tmp, sum

def merge_sort(in_lis):
    if len(in_lis) == 1:
        sum = 0
        return in_lis, sum
    if len(in_lis) > 1:
        (lis_a, sum_a) = merge_sort(in_lis[0: int(len(in_lis) / 2)])
        (lis_b, sum_b) = merge_sort(in_lis[int(len(in_lis)/2):])
        (lis, value) = merge_value(lis_a, lis_b)
        sum = sum_a + sum_b
        sum += value
        return lis, sum


if __name__ == "__main__":
    lis_a = [3, 2, 5, 9, 1]
    print(merge_value([3], [2, 1]))
    print(merge_sort(lis_a))
