def heapfy_b2h(heap):
    if len(heap) <= 2:
        return heap
    count = 1
    while count != len(heap):
        cur = count
        while cur > 1 and heap[cur] > heap[int(cur/2)]:
            tmp = heap[cur]
            heap[cur] = heap[int(cur/2)]
            heap[int(cur/2)] = tmp
            cur = int(cur/2)
        count += 1
    return heap

def heapfy_h2b(heap):
    if len(heap) <= 2:
        return heap
    count = 1
    while count <= int((len(heap)-1)/2):
        cur = count
        while cur <= int((len(heap)-1)/2) and (heap[cur] < heap[2*cur] or ((2*cur+1 < len(heap)) and heap[cur] < heap[2*cur+1])):
            if heap[2*cur] <= heap[2*cur+1]:
                tmp = heap[cur]
                heap[cur] = heap[2*cur+1]
                heap[2*cur+1] = tmp
                cur = 2*cur + 1
            else:
                tmp = heap[cur]
                heap[cur] = heap[2*cur]
                heap[2*cur] = tmp
                cur = 2*cur
        count += 1
    return heap

class PriorityQueue:
    def __init__(self):
        self.p_queue = ['guard']
        self.length = 1

    def enqueue(self, data):
        self.p_queue.append(data)
        self.length += 1
        if self.length == 2:
            return
        cur = self.length - 1
        while self.p_queue[cur] > self.p_queue[int(cur/2)]:
            tmp = self.p_queue[cur]
            self.p_queue[cur] = self.p_queue[int(cur/2)]
            self.p_queue[int(cur/2)] = tmp
            cur = int(cur/2)
        return

    # dequeue the root node of heap
    def dequeue(self):
        self.p_queue[1] = self.p_queue[self.length-1]
        self.p_queue.pop(self.length-1)

if __name__ == "__main__":
    sample = ["guard", 5, 4, 6, 9, 11, 1, 7, 0]
    output1 = heapfy_b2h(sample)
    print(output1)
    output2 = heapfy_h2b(sample)
    print(output2)

