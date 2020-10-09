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
        
if __name__ == "__main__":
    a = "mitcmux"
    b = "mtacnux"
    a += 'k'
    b += 'k'
    lwst_dist(a, b, 0)
    print(this_dist)
           