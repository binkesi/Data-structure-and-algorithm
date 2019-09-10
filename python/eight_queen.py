queen_list = [0, 0, 0, 0, 0, 0, 0, 0]
def cal8queens(row):
    if row == 8:
        print_queen(queen_list)
        return
    for column in range(8):
        if isOK(row, column):
            queen_list[row] = column
            cal8queens(row+1)

def isOK(row, column):
    leftup = column - 1
    rightup = column + 1
    for i in range(row-1, -1, -1):
        if queen_list[i] == column:
            return False
        if leftup >= 0:
            if queen_list[i] == leftup:
                return False
        if rightup < 8:
            if queen_list[i] == rightup:
                return False
        leftup -= 1
        rightup += 1
    return True


def print_queen(result):
    for row in range(0, 8):
        for column in range(0, 8):
            if result[row] == column:
                print("Q", end='')
            else:
                print("*", end='')
        print("\n")
    print("\n")

if __name__ == "__main__":
    cal8queens(0)