class Stack:
    def __init__(self, length: int):
        self.array = []
        self.length = length
        self.index = 0

    def push(self, data):
        if self.index >= self.length:
            raise IndexError
        else:
            self.array.append(data)
            self.index += 1
            #print(self.index)

    def pop(self):
        if self.index == 0:
            print("No data in stack.")
            return
        else:
            self.index -= 1
            return self.array.pop(self.index)

    def clear(self):
        while(self.index != 0):
            self.pop()


def main():
    my_stack = Stack(10)
    my_stack.push(2)
    my_stack.push(3)
    print(my_stack.pop())
    my_stack.push(8)
    my_stack.push(7)
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())

if __name__ == "__main__":
    main()
