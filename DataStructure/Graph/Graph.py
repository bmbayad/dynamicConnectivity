__author__ = 'bmbayad'
from Queue import QueueLinkedlist



class Graph(object):
    def __init__(self, IN):
        self.initialize_adj_list(int(IN.readline()))
        self.E = int(IN.readline())
        line = IN.readline()
        print "creation starts here"

        while line:
            print "my line: %s" %line
            a, b = map(int, line.split())
            print a, b
            self.addEdge(a,b)
            line = IN.readline()


    def initialize_adj_list(self,V):
        # creates a vertex without edge
        self.V = V
        self.E = 0
        self.adj = [None] * V
        for i in range(0,len(self.adj)):
            self.adj[i] = QueueLinkedlist()


    def V(self):
        # return number vertices
        pass

    def E(self):
        # return number of edges
        pass

    def addEdge(self, v, w):
        print "v: %d,  w:%d" %(v, w)
        # add edge v-w to this graph
        (self.adj[v]).enqueue(w)
        #print (self.adj[v]).size()
        (self.adj[w]).enqueue(v)

    def adj(self, v):
        # return a list of vertices adjacent to v1
        pass

    def toString(self):
        # string representation
        for item in range(0,len(self.adj)):
            print "vertex %d" %item
            print "adj size %d" %(self.adj[item]).size()




if __name__ == '__main__':
    f  = open(r'..\..\data\tinyg.txt',"r")
    client = Graph(f)
    client.toString()
    #print f