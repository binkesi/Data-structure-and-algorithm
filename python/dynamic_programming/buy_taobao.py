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

if __name__ == "__main__":
    commodity = [46, 18, 120, 79, 95, 37, 25, 80, 14, 66, 53, 39]
    limit = 100
    buy_taobao(commodity, 0, limit, 0)
    print(min_sum)