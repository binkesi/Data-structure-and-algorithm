def pay_coin(coin_list, amount):
    dp = [float("inf")] * (amount+1)
    for i in coin_list:
        dp[i] = 1
    for j in range(1, amount+1):
        for k in coin_list:
            if j-k > 0 and dp[j-k]!=float("inf"):
                dp[j] = min(dp[j], dp[j-k]+1)
    print(dp)
    return dp[-1]
    
if __name__ == "__main__":
    coin_list = [1, 3, 5]
    amount = 9
    print(pay_coin(coin_list, amount))