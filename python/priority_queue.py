def heapfy(heap):
    if heap.length <= 1:
        return


class PriorityQueue:
    def __init__(self):
        self.p_queue = ['guard']
        self.length = 1

    def enqueue(self, data):
        self.p_queue.append(data)
        self.length += 1
        if self.length == 2:
            return

