__author__ = 'bmbayad'

import settings


class QF(object):
    def __init__(self, vertices_num):
        self.unions = []
        self.size = vertices_num
        self.mainArray = [i for i in range(self.size)]
        self.levelsArray = [1 for i in range(self.size)]

    def connected(self, p, q):
        if self.mainArray[p] == self.mainArray[q]:
            return True
        else:
            return False

    def union(self, p, q):
        pid = self.mainArray[p]
        qid = self.mainArray[q]

        for idx, val in enumerate(self.mainArray):
            if self.mainArray[idx] == pid:
                self.mainArray[idx] = qid

    def find(self, p):
        while (p != self.mainArray[p]):
            p = self.mainArray[p]
        return self.mainArray[p]

    def count(self):
        return self.size

    def print_tree(self):
        print self.mainArray
