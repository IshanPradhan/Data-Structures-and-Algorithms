class Stack:
    def __init__(self,max_size):
        self.__max_size = max_size
        self.__elements = [None] * max_size
        self.__top = -1
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__top == self.__max_size-1):
            return True
        else:
            return False
    
    def is_empty(self):
        if(self.__top == -1):
            return True
        else:
            return False
    
    def push(self,element):
        if(self.is_full()):
            print('Stack is Full')
        else:
            self.__top += 1
            self.__elements[self.__top] = element
    
    def pop(self):
        if(self.is_empty()):
            print('Stack is Empty')
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data
    
    def display_stack(self):
        print('Elements of stack are: ')
        if(self.is_empty()):
            print('Stack is empty')
        else:
            ind = self.__top
            while(ind >= 0):
                print(self.__elements[ind])
                ind -= 1

if __name__ == "__main__":
    stack = Stack(5)
    print('Pushing 1 in Stack: \n')
    stack.push(1)
    print('Pushing 2 in Stack: \n')
    stack.push(2)
    stack.display_stack()
    print('\n')
    print('Popping the last Element')
    p = stack.pop()
    print('Element popped is ' + str(p))
    print('Pushing 3 in the Stack: \n')
    stack.push(3)
    stack.display_stack()
    print('\n')
    print('Pushing 5 in the Stack: \n')
    stack.push(5)
    print('Pushing apple in the stack')
    stack.push('apple')
    stack.display_stack()
