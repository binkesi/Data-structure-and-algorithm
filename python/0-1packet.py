import sys
sys.setrecursionlimit(1000000)

item_list = [15, 36, 7, 18, 26, 5, 51, 29, 10, 32]
max_weight = 100
maxW = 0
path = 10*[0]

def packet(i, cur_weight, tmp_path, it_list, n, max_w):
    global maxW, path
    if i == n or cur_weight == max_w:
        if cur_weight > maxW:
            maxW = cur_weight
            path = list(tmp_path)
            print(path)
        return
    tmp_path[i] = 0
    packet(i+1, cur_weight, tmp_path, it_list, n, max_w)

    if cur_weight + it_list[i] <= max_w:
        tmp_path[i] = 1
        packet(i+1, cur_weight + it_list[i], tmp_path, it_list, n, max_w)


if __name__ == "__main__":
    my_path = [0] * 10
    packet(0, 0, my_path, item_list, 10, max_weight)
    print(maxW)
    print(path)
