max_len = 0

def max_com(a, b, i, j, max_length):
    global max_len
    if i == (len(a)) or j == (len(b)):
        max_len = max(max_len, max_length)
        return
    if a[i] == b[j]:
        max_com(a, b, i+1, j+1, max_length+1)
    else:
        max_com(a, b, i+1, j, max_length)
        max_com(a, b, i, j+1, max_length)
        max_com(a, b, i+1, j+1, max_length)
        
def max_com_dp(a, b):
    dp = [[0]*len(a) for _ in range(len(b))]
    for i in range(len(a)):
        if a[i] == b[0]:
            for k in range(i, len(a)):
                dp[0][k] = 1
            break
        else:
            dp[0][i] = 0
    for j in range(len(b)):
        if b[j] == a[0]:
            for k in range(j, len(b)):
                dp[k][0] = 1
            break
        else:
            dp[j][0] = 0 
    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    for i in dp:
        print(i)
    com_str = ""
    a_ind = len(a)-1
    b_ind = len(b)-1
    while a_ind >= 0 and b_ind >= 0:
        print(a_ind, b_ind)
        if a[a_ind] == b[b_ind]:
            com_str += a[a_ind]
            if a_ind == 0 and b_ind == 0:
                break
            if a_ind >= 1 and b_ind >= 1 and dp[a_ind][b_ind]-1 == dp[a_ind -1][b_ind-1]:
                a_ind -= 1
                b_ind -= 1
            elif a_ind >= 1 and dp[a_ind][b_ind] == dp[a_ind -1][b_ind]:
                a_ind -= 1
            elif b_ind >= 1 and dp[a_ind][b_ind] == dp[a_ind][b_ind-1]: 
                b_ind -= 1
        else:
            if a_ind == 0 and b_ind == 0:
                break
            if a_ind >= 1 and b_ind >=1 and dp[a_ind][b_ind] == dp[a_ind-1][b_ind-1]:
                a_ind -= 1
                b_ind -= 1
            elif a_ind>= 1 and dp[a_ind][b_ind] == dp[a_ind-1][b_ind]:
                a_ind -= 1
            elif b_ind>= 1 and dp[a_ind][b_ind] == dp[a_ind][b_ind-1]:
                b_ind -= 1
    return com_str[::-1]
        
if __name__ == "__main__":
    a = "mtacnu"
    b = "mitcmu"
    max_com(a, b, 0, 0, 0)
    print(max_len)
    print(max_com_dp(a, b))