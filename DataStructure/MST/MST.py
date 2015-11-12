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

    def either(self):
        return self.v

    def other(self, v):
        if v == self.v:
            return self.w
        else:
            return self.v

    def compareTo(self, that_edge):
        if self.weight < that_edge.weight:
            return -1
        elif self.weight > that_edge.weight:
            return 1
        else:
            return 0

    def get_weight(self):
        pass

    def to_string(self):
        pass


class EdgeWeightedGraph(object):
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
        # print (self.adj[v]).size()
        (self.adj[w]).enqueue(e)

    def get_adj(self, v):
        # return a list of vertices adjacent to v1
        return self.adj[v]

    def get_adj_list(self, v):
        # return a list of vertices adjacent to v1
        return (self.adj[v]).get_list()

    def tostring(self):
        # string representation
        for item in range(0, len(self.adj)):
            print "vertex %d" % item
            # print "adj size %d" % (self.adj[item]).size()

    def show_graph(self):
        # draw the graph
        nx.draw(self.G, with_labels=True)
        # show the graph after addition of nodes
        plt.show()

    def get_edges(self):
        edges = []
        for i in range(0, self.get_V()):
            for g in self.get_adj_list(i):
                edges.append(g)
        return edges


class MST(object):
    def __init__(self, G):
        self.mst = []
        self.edges = sorted([e for e in G.get_edges()], key=lambda x: x.weight)
        print [x.weight for x in self.edges]
        uf = QF(len(self.edges))

        while len(self.edges) != 0 and len(self.mst) <= (G.get_V()-1):
            e = self.edges.pop(0)

            if not uf.connected(e.v,e.w):
                uf.union(e.v,e.w)
                self.mst.append(e)




    def get_edges(self):
        return self.mst


if __name__ == '__main__':
    f = open(r'..\..\data\tinyewg.txt', "r")
    g = EdgeWeightedGraph(f)
    # edgeitr = client.get_adj_list(0)
    # print [ (x.v,x.w,x.weight) for x in edgeitr]
    mst = MST(g)
    print [(m.v,m.w) for m in mst.get_edges()]


    # client.show_graph()

    # client.tostring()
    # temp = client.get_adj(237)
    # temp.print_queue()
    # print f
