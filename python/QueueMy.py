class MyQueue:
    def __init__(self, length):
        self.queue = []
        self.length = length
        self.head_index = 0
        self.tail_index = 0

    def enqueue(self, data):
        if self.tail_index == self.length:
            if self.head_index == 0:
                print("queue is full.")
                return
            else:
                for i in range(0, self.tail_index - self.head_index):
                    self.queue[i] = self.queue[self.head_index]
                    self.head_index += 1
                    self.tail_index -= 1
                self.head_index = 0
        self.queue.append(data)
        self.tail_index += 1

    def dequeue(self):
        if self.tail_index == 0:
            print("No data in queue")
            return
        else:
            ret = self.queue[self.head_index]
            self.head_index += 1
            print(ret)
            return ret


def main():
    my_queue = MyQueue(10)
    my_queue.enqueue(5)
    my_queue.enqueue(4)
    my_queue.enqueue(8)
    my_queue.dequeue()
    my_queue.enqueue(2)
    my_queue.enqueue(9)
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.enqueue(12)
    my_queue.enqueue(23)
    my_queue.enqueue(10)
    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue()

if __name__ == "__main__":
    main()