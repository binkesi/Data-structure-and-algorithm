# 0-1 packet backtracking method.
max_weight = 0
def packet(stones, index, max_w, cur_w):
    global max_weight
    if index == len(stones):
        max_weight = max(max_weight, cur_w)
        return
    packet(stones, index+1, max_w, cur_w)
    if cur_w + stones[index] <= max_w:
        packet(stones, index+1, max_w, cur_w+stones[index])

        
if __name__ == "__main__":
    stones = [2, 2, 4, 6, 3]
    packet(stones, 0, 9, 0)
    print(max_weight)