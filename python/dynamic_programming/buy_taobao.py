min_sum = float("inf")
def buy_taobao(commodity, index, limit, cur):
    global min_sum
    if index == len(commodity):
        return
    if cur >= limit:
        min_sum = min(cur, min_sum)
        return
    buy_taobao(commodity, index+1, limit, cur+commodity[index])
    buy_taobao(commodity, index+1, limit, cur)
    
def buy_taobao_dp(commodity, limit):
    m_sum = float("inf")
    all_sum = sum(commodity)
    dp = [[0] * all_sum for _ in range(len(commodity))]
    dp[0][0] = 1
    dp[0][commodity[0]] = 1
    for i in range(1, len(commodity)):
        for j in range(all_sum):
            if dp[i-1][j] == 1:
                dp[i][j] = dp[i-1][j]
        for j in range(all_sum):
            if j + commodity[i] < limit:
                if dp[i-1][j] == 1:
                    dp[i][j+commodity[i]] = dp[i-1][j]
            else:
                if dp[i-1][j] == 1:
                    m_sum = min(m_sum, j + commodity[i])
    return m_sum
            

if __name__ == "__main__":
    commodity = [46, 18, 120, 79, 95, 37, 25, 80, 14, 66, 53, 39]
    limit = 100
    buy_taobao(commodity, 0, limit, 0)
    print(min_sum)
    print(buy_taobao_dp(commodity, limit))