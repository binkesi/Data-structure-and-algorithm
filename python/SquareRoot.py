from python.Binary_search import binary_search
from functools import reduce

def cac_sum(input_list):
    sum = 0
    for i, x in enumerate(input_list):
        sum += x * (0.1 ** i)
    return sum

def square_root(num):
    if num == 1:
        return 1
    result_arr = []
    first_arr = [i for i in range(int(num/2)+1)]
    low = 0
    high = len(first_arr)-1
    while(low <= high):
        mid = low + ((high-low) >> 1)
        if mid * mid == int(num):
            result_arr.append(mid)
            break
        elif mid * mid < int(num) and (mid+1)*(mid+1) > int(num):
            result_arr.append(mid)
            break
        elif mid * mid > int(num) and (mid-1)*(mid-1) < int(num):
            result_arr.append(mid-1)
            break
        elif mid * mid < int(num) and (mid+1)*(mid+1) <= int(num):
            low = mid + 1
        elif mid * mid > int(num) and (mid - 1)*(mid - 1) >= int(num):
            high = mid - 1

    while len(result_arr) <= 6:
        ex_root = cac_sum(result_arr)
        low = 0
        high = 9
        while(low <= high):
            mid = int((low + high)/2)
            new_root = mid * (0.1**len(result_arr)) + ex_root
            low_root = (mid-1) * (0.1**len(result_arr)) + ex_root
            high_root = (mid+1) * (0.1**len(result_arr)) + ex_root
            if new_root * new_root == num:
                result_arr.append(mid)
                return cac_sum(result_arr)
            elif new_root * new_root < num and high_root * high_root > num:
                result_arr.append(mid)
                print(result_arr)
                break
            elif new_root * new_root > num and low_root * low_root < num:
                result_arr.append(mid - 1)
                print(result_arr)
                break
            elif new_root * new_root < num and high_root * high_root <= num:
                low = mid + 1
            elif new_root * new_root > num and low_root * low_root >= num:
                high = mid - 1

    result = cac_sum(result_arr)
    return result


if __name__ == "__main__":
    print(square_root(126))

