__author__ = 'bmbayad'
from Queue import QueueLinkedlist
import networkx as nx
import matplotlib.pyplot as plt

class Graph(object):

    def __init__(self, IN):
        #setup the graph
        self.G = nx.Graph()

        self.initialize_adj_list(int(IN.readline()))
        self.E = int(IN.readline())
        line = IN.readline()

        while line:
            a, b = map(int, line.split())
            #print a, b
            self.add_edge(a, b)
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

    def add_edge(self, v, w):
        #print "v: %d,  w:%d" % (v, w)
        self.G.add_edge(v,w)

        # add edge v-w to this graph
        (self.adj[v]).enqueue(w)
        # print (self.adj[v]).size()
        (self.adj[w]).enqueue(v)

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
            #print "adj size %d" % (self.adj[item]).size()

    def show_graph(self):
        #draw the graph
        nx.draw(self.G, with_labels=True)
        #show the graph after addition of nodes
        plt.show()

if __name__ == '__main__':
    f = open(r'..\..\data\tinyg.txt', "r")
    client = Graph(f)

    #client.tostring()
    #temp = client.get_adj(237)
    #temp.print_queue()
    # print f
