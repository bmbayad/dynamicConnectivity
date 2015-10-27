__author__ = 'bmbayad'

import LinkedList as ll


class StackLinkedlist(object):

    def __init__(self):
        self.linkedlist = ll.linkedlist()

    def is_empty(self):
        return self.linkedlist.first is None

    def size(self):
        return self.linkedlist.get_size()

    def push(self,item):
        self.linkedlist.insert_front(item)

    def pop(self):
        item = self.linkedlist.remove_front()
        return item