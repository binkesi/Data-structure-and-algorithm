class ListNode:
    def __init__(self, value=None, next_node=None):
        self._value = value
        self._next_node = next_node
        
    def __str__(self):
        return str(self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is None:
            self._value = None
        elif not isinstance(value, int):
            raise TypeError("Invalid value type.")
        else:
            self._value = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        if node is None:
            self._next_node = None
        elif not isinstance(node, ListNode):
            raise TypeError("Invalid node type.")
        else:
            self._next_node = node


class LinkedList:
    def __init__(self):
        self._guard_node = ListNode()
        self._head = self._guard_node
        
    def __str__(self):
        tmp = self._head
        list_str = ''
        while tmp.next_node is not None:
            list_str = list_str + str(tmp.next_node.value) + ' '
            tmp = tmp.next_node
        return list_str

    def search_by_value(self, value):
        if not isinstance(value, int):
            raise TypeError("Invalid search value.")
        search_ptr = self._guard_node
        while search_ptr.next_node is not None:
            if search_ptr.next_node.value == value:
                return search_ptr.next_node
            else:
                search_ptr = search_ptr.next_node
        return None

    @staticmethod
    def insert_after(list_node, insert_node):
        if not isinstance(insert_node, ListNode):
            raise TypeError("Invalid insert node type.")
        else:
            insert_node.next_node = list_node.next_node
            list_node.next_node = insert_node

    def reverse_list(self):
        ptr_1 = self._guard_node.next_node
        if ptr_1 is None:
            return
        ptr_2 = ptr_1.next_node
        if ptr_2 is None:
            self._guard_node.next_node = ptr_1
            return


if __name__ == "__main__":
    node1 = ListNode(5)
    node2 = ListNode(6)
    list1 = LinkedList()
    list1.insert_after(list1._head, node1)
    list1.insert_after(node1, node2)
    print(list1)
