def pay_coin(coin_list, amount):
    # put each element to "inf" so that we can easily use min() to get minium coins number.
    dp = [float("inf")] * (amount+1)
    for i in coin_list:
        dp[i] = 1
    for j in range(1, amount+1):
        for k in coin_list:
            if j-k > 0 and dp[j-k]!=float("inf"):
                dp[j] = min(dp[j], dp[j-k]+1)
    # set dp[0] to 0, as if we want to pay 0, we need 0 coins.
    dp[0] = 0
    cur_value = amount
    cur_num = dp[-1]
    coins = []
    for k in range(len(dp)-1, -1, -1):
        if cur_num == 0:
            break
        if dp[k] == cur_num-1:
            for i in coin_list:
                if cur_value-k == i:
                    coins.append(i)
                    cur_num -= 1
                    cur_value -= i
    return coins
    
if __name__ == "__main__":
    coin_list = [1, 3, 5]
    amount = 9
    print(pay_coin(coin_list, amount))