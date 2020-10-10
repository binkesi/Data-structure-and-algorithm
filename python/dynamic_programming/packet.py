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

# 0-1 packet dp method, two dimesion.
def packet_dp(stones, max_w):
    dp = [[0]*(max_w+1) for _ in range(len(stones))]
    dp[0][0] = 1
    if stones[0] <= max_w:
        dp[0][stones[0]] = 1
    for i in range(1, len(stones)):
        for j in range(max_w+1):
            # do not put in ith. stone.
            if dp[i-1][j] == 1:
                dp[i][j] = dp[i-1][j]
            # put in ith. stone.
            if dp[i-1][j] == 1 and j+stones[i] <= max_w:
                dp[i][j+stones[i]] = dp[i-1][j]
    for k in range(max_w, 0, -1):
        if dp[-1][k] == 1:
            return k
            
# 0-1 packet dp method, one dimesion.
def packet_dp_oned(stones, max_w):
    dp = [0] * (max_w+1)
    dp[0] = 1
    if stones[0] <= max_w:
        dp[stones[0]] = 1
    for i in range(1, len(stones)):
        for j in range(max_w, -1, -1):
            if dp[j] == 1 and j+stones[i] <= max_w:
                dp[j+stones[i]] = 1
    for k in range(max_w, -1, -1):
        if dp[k] == 1:
            return k

# 0-1 packet dp with value.            
def packet_dp_value(stones, values, max_w):
    dp = [-1] * (max_w+1)
    dp[0] = 0
    if stones[0] <= max_w:
        dp[stones[0]] = values[0]
    for i in range(1, len(stones)):
        for j in range(max_w, -1, -1):
            if dp[j] != -1 and j+stones[i] <= max_w:
                dp[j+stones[i]] = max(dp[j+stones[i]], dp[j]+values[i])
    return max(dp)
        
        
if __name__ == "__main__":
    stones = [2, 2, 4, 6, 3]
    values = [3, 4, 8, 9, 6]
    max_w = 9
    packet(stones, 0, max_w, 0)
    print(max_weight)
    print(packet_dp(stones, max_w))
    print(packet_dp_oned(stones, max_w))
    print(packet_dp_value(stones, values, max_w))