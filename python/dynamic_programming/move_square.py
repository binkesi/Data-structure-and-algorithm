def move_square(square):
    dp = [[0]*len(square[0]) for _ in range(len(square))]
    dp[0][0] = square[0][0]
    for i in range(1, len(square[0])):
        dp[0][i] = dp[0][i-1] + square[0][i]
    for j in range(1, len(square)):
        dp[j][0] = dp[j-1][0] + square[j][0]
    for i in range(1, len(square[0])):
        for j in range(1, len(square)):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + square[i][j]
    print(dp)
    cur_v = dp[-1][-1]
    path = []
    x = len(dp)-1
    y = len(dp[0])-1
    while cur_v > 0:
        if dp[x-1][y] == cur_v - square[x][y]:
            path.append(square[x][y])
            cur_v -= square[x][y]
            x -= 1
        elif dp[x][y-1] == cur_v - square[x][y]:
            path.append(square[x][y])
            cur_v -= square[x][y]
            y -= 1
        else:
            path.append(square[0][0])
            break
    path.reverse()
    return path
            
if __name__ == "__main__":
    square = [[1, 3, 5, 9], [2, 1, 3, 4], [5, 2, 6, 7], [6, 8, 4, 3]]
    print(move_square(square))