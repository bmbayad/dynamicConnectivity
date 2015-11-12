__author__ = 'bmbayad'
from Graph import Graph
from DiGraph import DiGraph


class DepthFirstSearch(object):
    def __init__(self, graph, source):
        self.count = 0
        self.marked = [False] * graph.get_V()
        self.dfs(graph, source)

    def dfs(self, graph, vertex):
        self.marked[vertex] = True
        self.count += 1
        for v in graph.get_adj_list(vertex):

            if self.marked[v] is not True:
                #print "%d -- %d" % (vertex, v)
                self.dfs(graph, v)
            else:
                #print "%d -- %d has been visited already" % (vertex, v)
                pass


class DepthFirstPaths(object):
    def __init__(self, graph, source):
        self.count = 0

        self.marked = [False] * graph.get_V()
        self.edge_to = [None] * graph.get_V()
        self.source = source

        self.dfs(graph, source)

    def dfs(self, graph, vertex):
        self.marked[vertex] = True
        self.count += 1
        for v in graph.get_adj_list(vertex):

            if self.marked[v] is not True:
                #print "%d -- %d" % (v, vertex)
                self.edge_to[v] = vertex
                self.dfs(graph, v)

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
    #f = open(r'..\..\data\mediumg.txt', "r")
    #graph = Graph(f)

    # dfs = DepthFirstSearch(graph, 0)


    #dfs = DepthFirstPaths(graph, 0)
    #print dfs.edge_to
    #arr = dfs.path_to(3)
    #print arr[::-1]
    #graph.show_graph()

    f = open(r'..\..\data\tinyDG.txt', "r")
    graph = DiGraph(f)
    client = DepthFirstPaths(graph,0)
    print client.edge_to

