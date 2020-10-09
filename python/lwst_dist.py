min_dist = float('inf')
def lwst_dist(stra, strb, i, j, edist):
    global min_dist
    if i == len(stra) or j == len(strb):
        if i == len(stra):
            edist += (len(strb) - j)
        if i == len(strb):
            edist += (len(stra) - i)
        if edist < min_dist:
            min_dist = edist
        return
    if stra[i] == strb[j]:
        lwst_dist(stra, strb, i+1, j+1, edist)
    else:
        lwst_dist(stra, strb, i, j+1, edist+1)
        lwst_dist(stra, strb, i+1, j, edist+1)
        lwst_dist(stra, strb, i+1, j+1, edist+1)
        
def l_dist(stra, strb):
    a = len(stra)
    b = len(strb)
    dist = [[0]*a for _ in range(b)]
    if stra[0] == strb[0]:
        dist[0][0] = 0
    else:
        dist[0][0] = 1
    for i in range(1, a):
        dist[0][i] = dist[0][i-1] + 1
    for j in range(1, b):
        dist[j][0] = dist[j-1][0] + 1
    for m in range(1, b):
        for n in range(1, a):
            if stra[n] == strb[m]:
                dist[m][n] = min(dist[m-1][n-1], dist[m-1][n]+1, dist[m][n-1]+1)
            else:
                dist[m][n] = min(dist[m-1][n-1]+1, dist[m-1][n]+1, dist[m][n-1]+1)
    return dist[b-1][a-1]
        
if __name__ == "__main__":
    lwst_dist('mucfgh', 'mrcagb', 0, 0, 0)
    print(l_dist('mucfgh', 'mrcagb'))
    print(min_dist)
    