from python.MyLinkedList import LinkedList
from python.MyLinkedList import ListNode

class MyGraph:
    def __init__(self):
        self.v_num = 0
        self.n_metric = []

    def add_vertex(self):
        new_vertex = LinkedList()
        self.n_metric.append(new_vertex)
        self.v_num += 1

    def add_edge(self, edge):
        if not isinstance(edge, tuple):
            raise TypeError("Invalid edge type.")
        if edge[0] >= len(self.n_metric) or edge[1] >= len(self.n_metric):
            print("Invalid edge data input {}.".format(edge))
            return
        self.n_metric[edge[0]].insert_after(self.n_metric[edge[0]]._head, ListNode(edge[1]))
        self.n_metric[edge[1]].insert_after(self.n_metric[edge[1]]._head, ListNode(edge[0]))

    def output_vertex(self):
        for i in range(self.v_num):
            print(i)

    def output_edge(self):
        for vertex in self.n_metric:
            v_data = self.n_metric.index(vertex)
            v_node = vertex._head.next_node
            while v_node is not None:
                edge = (v_data, v_node.value)
                print(edge)
                v_node = v_node.next_node

    def bfs(self, v_start, v_dest):
        if v_start == v_dest:
            print((v_start, v_dest))
            return
        visited = [False] * self.v_num
        visited[v_start] = True
        v_queue = []
        v_queue.append(v_start)
        v_prev = [-1]*self.v_num
        while len(v_queue) != 0:
            cur_node = self.n_metric[v_start]._head
            while cur_node.next_node is not None:
                if visited[cur_node.next_node.value] == False:
                    visited[cur_node.next_node.value] = True
                    v_prev[cur_node.next_node.value] = v_start



if __name__ == "__main__":
    sample_graph = MyGraph()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_edge((0, 1))
    sample_graph.add_edge((0, 2))
    sample_graph.add_edge((2, 3))
    sample_graph.add_edge((3, 4))
    sample_graph.add_edge((1, 3))
    sample_graph.add_edge((4, 2))
    sample_graph.add_edge((3, 0))
    sample_graph.add_edge((5, 0))
    sample_graph.output_vertex()
    sample_graph.output_edge()
    abc = [False, 5]
    print(abc)
