__author__ = 'bmbayad'
from Graph import Graph


class CC(object):
    def __init__(self, graph, source):
        self.id = [None] * graph.get_V()
        self.marked = [False] * graph.get_V()
        self.count = 0

        for item in range(0, graph.get_V()):
            if self.marked[item] is not True:
                self.dfs(graph, item)
                self.count += 1

    def dfs(self, graph, vertex):
        self.marked[vertex] = True
        self.id[vertex] = self.count

        for v in graph.get_adj_list(vertex):

            if self.marked[v] is not True:
                self.dfs(graph, v)


if __name__ == '__main__':
    f = open(r'..\..\data\tinyg.txt', "r")
    graph = Graph(f)
    dfs = CC(graph, 0)
    print dfs.id
