class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
     
    def __str__(self):
        return str(self.value)
        

class LinkList:
    def __init__(self):
        self.head = None
        
    def insert(self, node, ptr=None):
        if self.head is None:
            self.head = node
        elif ptr is None:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = node
        elif ptr.next is None:
            ptr.next = node
        else:
            node.next = ptr.next
            ptr.next = node
    
    def delete(self, node):
        tmp = self.head
        while tmp != node:
            tmp = tmp.next
        if node.next is None:
            tmp = None
        else:
            tmp = node.next
            
    def __str__(self):
        tmp = self.head
        result = []
        while tmp is not None:
            result.append(str(tmp.value))
            tmp = tmp.next
        return ' '.join(result)
            

def ReverseList(list_a):
    head = list_a.head
    if head is None or head.next is None:
        return
    tmp = head.next
    head.next = None
    while tmp is not None:
        med = tmp.next
        tmp.next = head
        head = tmp
        tmp = med
    list_a.head = head
    
def CircleCheck(list_a):
    head = list_a.head
    if head is None or head.next is None:
        return False
    low_re = quick_re = head
    while quick_re is not None and quick_re.next is not None:
        low_re = low_re.next
        quick_re = quick_re.next.next
        if low_re == quick_re:
            return True
    return False
    
def MergeTwo(list_a, list_b):
    head_a = list_a.head
    head_b = list_b.head
    if head_a is None:
        return head_b
    if head_b is None:
        return head_a
    if head_a.value < head_b.value:
        hold = head_a
        lower_step = head_a.next
    else:
        hold = head_b
        lower_step = head_b.next
        tmp = head_a
        head_a = head_b
        head_b = tmp
    while lower_step is not None:
        if lower_step.value < head_b.value:
            hold = lower_step
            lower_step = lower_step.next
        else:
            hold.next = head_b
            hold = head_b
            head_b = lower_step
            lower_step = hold.next
    hold.next = head_b
    return list_a
    
def DeleteLastN(list_a, n):
    head = list_a.head
    if head is None:
        return
    total = 0
    while head is not None:
        total += 1
        head = head.next
    if n > total:
        print("Not enough nodes.")
        return
    if n == total:
        list_a.head = list_a.head.next
        return
    head = list_a.head
    dif = total - n
    while dif != 1:
        head = head.next
        dif -= 1
    head.next = head.next.next

def find_mid(list_a):
    head = list_a.head
    if head is None:
        print("No node in the link list.")
        return None
    if head.next is None:
        return head
    low_re = quick_re = head
    while quick_re.next is not None and quick_re.next.next is not None:
        low_re = low_re.next
        quick_re = quick_re.next.next
    return low_re

if __name__ == "__main__":
    list1 = LinkList()
    list2 = LinkList()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)    
    list1.insert(node1)
    list1.insert(node6)
    list1.insert(node8)
    list2.insert(node2)
    list2.insert(node3)
    list2.insert(node4)
    list2.insert(node5)
    list2.insert(node7)
    print(list1)
    print(CircleCheck(list1))
    print(list2)
    list3 = MergeTwo(list1, list2)
    print(list3)
    node_mid = find_mid(list3)
    print(node_mid)    
    DeleteLastN(list3, 7)
    print(list3)
    node_mid = find_mid(list3)
    print(node_mid)