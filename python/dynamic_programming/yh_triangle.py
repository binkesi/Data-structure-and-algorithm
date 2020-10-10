def yh_triangle(tri):
    if len(tri) == 1:
        return tri[0][0]
    dp = tri
    for i in tri:
        for j in i:
            j = 0
    dp[0][0] = tri[0][0]
    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            if j == 0:
                dp[i][j] = dp[i-1][0] + tri[i][j]
            elif j == len(tri[i])-1:
                dp[i][j] = dp[i-1][-1] + tri[i][j]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]
    return min(dp[-1])
    
if __name__ == "__main__":
    test_tri = [[5], [1, 3], [8, 6, 2], [4, 9, 6, 7]]
    print(yh_triangle(test_tri))