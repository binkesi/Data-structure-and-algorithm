import time
stage_dict = {}

def stage(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2

    if (stage_dict.get(num) is not None):
        return stage_dict.get(num)
    ret = stage(num-1) + stage(num-2)
    stage_dict[num] = ret
    return ret

if __name__ == "__main__":
    beg = time.perf_counter()
    print(stage(30))
    end = time.perf_counter()
    print(end - beg)

