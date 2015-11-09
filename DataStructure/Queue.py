__author__ = 'bmbayad'
import LinkedList

class QueueLinkedlist(object):

    def __init__(self):
        self.linkedlist = LinkedList.linkedlist()

    def enqueue(self,item):
        self.linkedlist.insert_end(item)

    def dequeue(self):
        item = self.linkedlist.remove_front()
        return item

    def is_empty(self):
        return self.linkedlist.first is None

    def size(self):
        return  self.linkedlist.get_size()

    def print_queue(self):
        self.linkedlist.print_linkedlist()

    def get_list(self):
        return self.linkedlist.get_linkedlist_iterator()
