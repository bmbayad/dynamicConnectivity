__author__ = 'bmbayad'


class Node(object):
    def __init__(self, data=None):
        self.item = data
        self.node = None


class linkedlist(object):
    def __init__(self):
        self.first = None
        self.size = 0

    def insert_front(self, data):
        new_first = Node(data)
        new_first.node = self.first
        self.first = new_first
        self.size += 1

    def insert(self, data, next_node):
        if next_node.node is not None:
            self.insert(data, next_node.node)
        else:
            next_node.node = Node(data)

    def insert_end(self, data):
        if self.first is not None:
            self.insert(data, self.first)
        else:
            self.first = Node(data)
        self.size += 1

    def remove_front(self):
        if self.first is not None:
            item = self.first.item
            next_first = self.first.node
            self.first.node = None
            self.first = next_first
            self.size -= 1
            return  item

    def remove(self, previous_node, next_node):

        if next_node.node is not None:
            item = self.remove(next_node, next_node.node)
        else:
            item = previous_node.node.item
            previous_node.node = None
        return item

    def remove_end(self):
        if self.first is None:
            print "list is empty"
            item = None
        elif self.first.node is None:
            item = self.first.item
            self.first = None
            self.size -= 1
        else:
            item = self.remove(self.first, self.first.node)
            self.size -= 1
        return item

    def print_linkedlist(self):
        curr = self.first
        while curr is not None:
            print curr.item
            curr = curr.node

    def get_size(self):
        return self.size
