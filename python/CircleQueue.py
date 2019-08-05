class CircleQueue:
    def __init__(self, length):
        self.length = length
        self.head_index = 0
        self.tail_index = 0
        self.queue = [None]*length

    def enqueue(self, data):
        if (self.tail_index + 1) % self.length == self.head_index:
            print("Queue is full.")
            return
        else:
            self.queue.insert(self.tail_index, data)
            self.tail_index = (self.tail_index + 1) % self.length

    def dequeue(self):
        ret = self.queue[self.head_index]
        self.head_index = (self.head_index + 1) % self.length
        print(ret)
        return ret

def main():
    my_queue = CircleQueue(10)
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

