this_dist = float("inf")
def lwst_dist(a, b, init_dist):
    global this_dist
    if len(a) == 1:
        init_dist += (len(b)-1)
        this_dist = min(init_dist, this_dist)
        return
    if len(b) == 1:
        init_dist += (len(a)-1)
        this_dist = min(init_dist, this_dist)
        return
    if a[0] == b[0]:
        lwst_dist(a[1:], b[1:], init_dist)
    else:
        lwst_dist(a[1:], b, init_dist+1)
        lwst_dist(a, b[1:], init_dist+1)
        lwst_dist(a[1:], b[1:], init_dist+1)
        
def lwst_dist_dp(a, b):
    dp = [[0]*len(a) for _ in range(len(b))]
    for i in range(len(a)):
        if a[i] == b[0]:
            dp[0][i] = i
        # when i == 0, will use dp[0][-1], should notice this situation, anyway its value is right.
        else:
            dp[0][i] = dp[0][i-1] + 1
    for j in range(len(b)):
        if b[j] == a[0]:
            dp[j][0] = j
        else:
            dp[j][0] = dp[j-1][0]+1
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    return dp[-1][-1]
        
if __name__ == "__main__":
    a = "aitcmux"
    b = "mtacnux"
    print(lwst_dist_dp(a, b))    
    a += 'k'
    b += 'k'
    lwst_dist(a, b, 0)
    print(this_dist)
           