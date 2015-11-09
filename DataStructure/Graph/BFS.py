__author__ = 'bmbayad'
from Graph import Graph
from Queue import QueueLinkedlist

class BreadthFirstPaths(object):
    '''
        To find the shortest path
    '''
    def __init__(self, graph, source):

        self.queue = QueueLinkedlist()
        self.marked = [False] * graph.get_V()
        self.edge_to = [None] * graph.get_V()
        self.source = source

        self.bfs(graph, source)

    def bfs(self, graph, vertex):
        self.marked[vertex] = True
        self.queue.enqueue(self.source)
        while not self.queue.is_empty():
            v = self.queue.dequeue()
            for w in graph.get_adj_list(v):
                if self.marked[w] is False:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    self.queue.enqueue(w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if self.has_path_to(v) is False: return None
        arr = []
        x = v
        while x != self.source:
            arr.append(x)
            x = self.edge_to[x]
        arr.append(self.source)
        return arr


if __name__ == '__main__':
    f = open(r'..\..\data\tinyg.txt', "r")
    graph = Graph(f)
    bds = BreadthFirstPaths(graph,0)
    print bds.path_to(4)

