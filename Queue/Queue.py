class Queue:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0
    
    def get_maxsize(self):
        return self.__max_size
    
    def isFull(self):
        if(self.__rear == self.__max_size - 1):
            return True
        else:
            return False

    def isEmpty(self):
        if(self.__rear == -1):
            return True
        else:
            return False
    
    def enqueue(self,element):
        if(self.isFull()):
            print('Queue is Full')
        else:
            self.__rear += 1
            self.__elements[self.__rear] = element
    
    def dequeue(self):
        if(self.isEmpty()):
            print('Queue is Empty')
        else:
            element = self.__elements[self.__front]
            self.__front += 1
            return element
    
    def display_queue(self):
        print('Elements in queue are: \n')
        position = self.__front
        while(position <= self.__rear):
            print(self.__elements[position])
            position += 1

if __name__ == "__main__":
    queue = Queue(5)
    print('Enqueing 1 in the Queue: \n')
    queue.enqueue(1)
    print('Enqueing 2 in the Queue: \n')
    queue.enqueue(2)
    queue.display_queue()
    p = queue.dequeue()
    print('Dequeueing {} from the queue: \n'.format(p))
    print('Enqueueing 3 in the queue')
    queue.enqueue(3)
    queue.display_queue()
