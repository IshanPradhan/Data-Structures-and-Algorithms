class Node: 

	def __init__(self, data): 
		self.data = data 
		self.next = None 


class LinkedList: 

	def __init__(self): 
		self.head = None

# This method is used to traverse in the list and print the data in the list

	def printList(self): 
		temp = self.head 
		while (temp): 
			print(temp.data,end=' ') 
			temp = temp.next

if __name__ == '__main__':
    ll = LinkedList()

    ll.head = Node(1)
    second =  Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.printList()
    print('\n')
