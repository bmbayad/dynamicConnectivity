__author__ = 'bmbayad'
import networkx as nx
import matplotlib.pyplot as plt
from Queue import QueueLinkedlist
from quickfind1 import QF


class Edge(object):
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def edge_from(self):
        return self.v

    def edge_to(self):
        return self.w

    def get_weight(self):
        return self.weight


class EdgeWeightedDiGraph(object):
    def __init__(self, IN):
        # setup the graph
        self.G = nx.Graph()

        self.initialize_adj_list(int(IN.readline()))
        self.E = int(IN.readline())
        line = IN.readline()

        while line:
            a, b, c = line.split()
            a = int(a)
            b = int(b)
            c = float(c)

            print a, b, c
            self.add_edge(a, b, c)
            line = IN.readline()

    def initialize_adj_list(self, V):
        # creates a vertex without edge
        self.V = V
        self.E = 0
        self.adj = [None] * V
        for i in range(0, len(self.adj)):
            self.adj[i] = QueueLinkedlist()

    def get_V(self):
        # return number vertices
        return self.V

    def get_E(self):
        # return number of edges
        return self.E

    def add_edge(self, v, w, weight):
        # print "v: %d,  w:%d" % (v, w)
        self.G.add_edge(v, w)
        e = Edge(v, w, weight)
        # add edge v-w to this graph
        (self.adj[v]).enqueue(e)

    def get_adj_list(self, v):
        # return a list of vertices adjacent to v1
        return (self.adj[v]).get_list()

    def show_graph(self):
        nx.draw(self.G, with_labels=True)
        plt.show()


# shortest path class
class SP(object):
    def __init__(self, G, source):
        self.mst = []
        self.edges = sorted([e for e in G.get_edges()], key=lambda x: x.weight)
        print [x.weight for x in self.edges]
        uf = QF(len(self.edges))

        while len(self.edges) != 0 and len(self.mst) <= (G.get_V() - 1):
            e = self.edges.pop(0)

            if not uf.connected(e.v, e.w):
                uf.union(e.v, e.w)
                self.mst.append(e)

    def dist_to(self, v):
        return 0

    def path_to(self, v):
        path  = []
        return 0


if __name__ == '__main__':
    f = open(r'..\..\data\tinyewg.txt', "r")
    g = EdgeWeightedDiGraph(f)
    source = 0
    sp = SP(g, 0)
