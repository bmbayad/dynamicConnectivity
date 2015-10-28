__author__ = 'bmbayad'

import Stack
import Queue
def run():
    stack = Stack.StackLinkedlist()
    stack.push("a")
    stack.push("b")
    print stack.size()
    item = stack.pop()
    print item
    item = stack.pop()
    print item

    queue = Queue.QueueLinkedlist()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    item = queue.dequeue()
    print item

if __name__ == '__main__':
    run()
