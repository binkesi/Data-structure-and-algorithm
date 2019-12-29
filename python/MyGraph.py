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

    # breadth-first-search
    def bfs(self, v_start, v_dest):
        if v_start == v_dest:
            print((v_start, v_dest))
            return
        visited = [False] * self.v_num
        visited[v_start] = True
        v_queue = [v_start]
        v_prev = [-1]*self.v_num
        while len(v_queue) != 0:
            for v in v_queue:
                cur_node = self.n_metric[v]._head
                visited[v] = True
                while cur_node.next_node is not None:
                    if visited[cur_node.next_node.value] == False:
                        v_prev[cur_node.next_node.value] = v
                        v_queue.append(cur_node.next_node.value)
                        visited[cur_node.next_node.value] = True
                    cur_node = cur_node.next_node
                v_queue.remove(v)
            if v_dest in v_queue:
                v_queue.clear()
        print(v_prev)
        self.print_road(v_prev, v_start, v_dest)

    def print_road(self, v_prev, v_start, v_dest):
        road = [v_dest]
        while v_prev[v_dest] != -1 and v_dest != v_start:
            road.append(v_prev[v_dest])
            v_dest = v_prev[v_dest]
        road.reverse()
        for v in road:
            print(v)

    # depth-first-search
    def dfs(self, v_start, v_dest):
        if v_start == v_dest:
            print((v_start, v_dest))
            return
        visited = [False] * self.v_num
        visited[v_start] = True
        v_prev = [-1]*self.v_num
        self.recursive_dfs(v_start, v_dest, visited, v_prev)
        self.print_road(v_prev, v_start, v_dest)

    def recursive_dfs(self, v_start, v_dest, visited, v_prev):
        if v_start == v_dest:
            return
        cur_node = self.n_metric[v_start]._head
        rec = True
        while cur_node.next_node is not None:
            next_v = cur_node.next_node.value
            if visited[next_v] is False:
                rec = False
                visited[next_v] = True
                v_prev[next_v] = v_start
                self.recursive_dfs(next_v, v_dest, visited, v_prev)
                break
            else:
                cur_node = cur_node.next_node
        if rec:
            v_start = v_prev[v_start]
            self.recursive_dfs(v_start, v_dest, visited, v_prev)


if __name__ == "__main__":
    sample_graph = MyGraph()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_vertex()
    sample_graph.add_edge((0, 1))
    sample_graph.add_edge((0, 2))
    sample_graph.add_edge((1, 4))
    sample_graph.add_edge((2, 4))
    sample_graph.add_edge((1, 3))
    sample_graph.add_edge((2, 5))
    sample_graph.add_edge((4, 6))
    sample_graph.add_edge((4, 7))
    sample_graph.add_edge((3, 6))
    sample_graph.add_edge((5, 7))
    sample_graph.add_edge((6, 8))
    sample_graph.add_edge((7, 8))
    sample_graph.output_vertex()
    sample_graph.output_edge()
    sample_graph.bfs(0, 4)
    print("=====")
    sample_graph.dfs(0, 4)

