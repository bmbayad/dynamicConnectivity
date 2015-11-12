__author__ = 'bmbayad'
from Graph import Graph
from DiGraph import DiGraph
from Queue import QueueLinkedlist

class BreadthFirstPaths(object):
    '''
        To find the shortest path
    '''
    def __init__(self, graph, source):

        self.queue = QueueLinkedlist()
        self.marked = [False] * graph.get_V()
        self.edge_to = [None] * graph.get_V()
        self.distance_to = [-1]*graph.get_V()
        self.count = 0
        self.source = source

        self.bfs(graph, source)

    def bfs(self, graph, vertex):
        self.marked[vertex] = True
        self.queue.enqueue(self.source)
        count = 0
        while not self.queue.is_empty():
            v = self.queue.dequeue()
            self.distance_to[v] = count
            count += 1
            for w in graph.get_adj_list(v):
                if self.marked[w] is False:
                    self.edge_to[w] = v
                    self.marked[w] = True
                    print "frlm %d vertex: %d count: %d" %(v, w, count)
                    self.distance_to[w] = count
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
    #f = open(r'..\..\data\tinyg.txt', "r")
    #graph = Graph(f)
    #bds = BreadthFirstPaths(graph,0)
    #print bds.path_to(4)

    f = open(r'..\..\data\tinydg2.txt', "r")
    graph = DiGraph(f)
    bds = BreadthFirstPaths(graph,0)
    print bds.path_to(5 )
    print bds.distance_to
