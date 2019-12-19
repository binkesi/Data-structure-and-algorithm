def heapfy_h2b(heap):
    count = int((len(heap)-1)/2)
    while count >= 1:
        cur = count
        while True:
            if cur > int((len(heap)-1)/2):
                break
            maxpos = cur
            if (heap[cur] < heap[cur*2]):
                maxpos = cur*2
            if (cur*2+1 < len(heap) and heap[maxpos] < heap[cur*2+1]):
                maxpos = cur*2+1
            if maxpos == cur:
                break
            tmp = heap[cur]
            heap[cur] = heap[maxpos]
            heap[maxpos] = tmp
            cur = maxpos
        count -= 1
    return heap

def heap_sort(heap):
    sorted_heap = heapfy_h2b(heap)
    sorted_list = []
    while len(sorted_heap) >= 2:
        sorted_list.append(sorted_heap.pop(1))
        heapfy_h2b(sorted_heap)
    return sorted_list

class PriorityQueue:
    def __init__(self):
        self.p_queue = ['guard']

    def enqueue(self, data):
        self.p_queue.append(data)
        if len(self.p_queue) == 2:
            return
        cur = len(self.p_queue) - 1
        while self.p_queue[cur] > self.p_queue[int(cur/2)]:
            tmp = self.p_queue[cur]
            self.p_queue[cur] = self.p_queue[int(cur/2)]
            self.p_queue[int(cur/2)] = tmp
            cur = int(cur/2)

    # dequeue the root node of heap
    def dequeue(self):
        if len(self.p_queue) == 2:
            self.p_queue.pop(len(self.p_queue)-1)
            return
        self.p_queue[1] = self.p_queue[len(self.p_queue)-1]
        self.p_queue.pop(len(self.p_queue)-1)
        i = 1
        while i <= int((len(self.p_queue)-1)/2):
            maxpos = i
            if(i*2 < len(self.p_queue) and self.p_queue[i] < self.p_queue[i*2]):
                maxpos = i*2
            elif(i*2+1 < len(self.p_queue) and self.p_queue[i] < self.p_queue[i*2+1]):
                maxpos = i*2+1
            if maxpos == i:
                break
            tmp = self.p_queue[i]
            self.p_queue[i] = self.p_queue[maxpos]
            self.p_queue[maxpos] = tmp
            i = maxpos

if __name__ == "__main__":
    sample = ["guard", 5, 4, 6, 9, 11, 1, 7, 0]
    output2 = heapfy_h2b(sample)
    print(output2)
    my_priority = PriorityQueue()
    my_priority.p_queue = output2
    my_priority.dequeue()
    print(my_priority.p_queue)
    print(heap_sort(my_priority.p_queue))

