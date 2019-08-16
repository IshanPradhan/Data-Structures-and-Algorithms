class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None 


class LinkedList: 
 
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next

    def insert_in_beg(self,new_data):
        new_node = Node(new_data)
        new_node.next =self.head
        self.head = new_node 
    
    def insert_in_between(self,prev_node,new_data):
        if(prev_node is None):
            print('Previous node is not in the linkedlist')
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def insert_at_end(self,new_data):
        new_node = Node(new_data)
        if(self.head is None):
            self.head = new_node
            return 
        
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_node

if __name__ == '__main__':
    ll = LinkedList()

    ll.head = Node(1)
    second =  Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third
    
    print('Original LinkedList is: \n')
    
    ll.printList()


    print('\nIntersting 7 in the Beginning: \n')

    ll.insert_in_beg(7)

    ll.printList()

    print('\nInsert 6 at third position: \n')
    ll.insert_in_between(ll.head.next,6)

    ll.printList()

    print('\nInsert 10 at the end: \n')

    ll.insert_at_end(10)

    ll.printList()