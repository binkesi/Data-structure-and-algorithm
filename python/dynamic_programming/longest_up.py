def longest_up(ser):
    dp = [1] * len(ser)
    for i in range(1, len(ser)):
        for k in range(i):
            if ser[i] > ser[k]:
                dp[i] = max(dp[i], dp[k]+1)
    print(dp)
    lis = []
    max_len = max(dp)
    for i in range(len(dp)-1, -1, -1):
        if max_len == 0:
            break
        if dp[i] == max_len:
            lis.append(ser[i])
            max_len -= 1
    lis.reverse()
    return lis
    
    
if __name__ == "__main__":
    ser = [2, 5, 4, 3, 7, 9, 1, 3, 12, 13]
    print(longest_up(ser))