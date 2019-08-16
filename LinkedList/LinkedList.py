class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':

    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    '''
    The linkedlist looks like this at this stage
    _______     ________    ________
    |1|None|    |2|None|    |3|None|
    |__|___|    |_|____|    |_|____|
    There is no connectivity between them yet
    '''
    ll.head.next = second
    '''
    Now next of node 1 refers to the second Node
    _____    ________    ________
    |1|0| -> |2|None|    |3|None|
    |_|_|    |_|____|    |_|____|
     '''
    second.next = third
    '''
    Now next of node 2 refers to the third Node
    _____    _____    ________
    |1|0| -> |2|0| -> |3|None|
    |_|_|    |_|_|    |_|____|

    '''
    