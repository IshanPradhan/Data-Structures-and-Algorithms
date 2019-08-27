import random

def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    mid=n//2
    for _ in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1
    return list_of_elements

li = initialize_list_of_elements(10)

print('Randomly Generated list is: {}\n'.format(li))

random_value = random.choice(li)

print('Random Value chosen from the list is {}\n'.format(random_value))

for i in range(0,len(li)-1):
    if(random_value == li[i]):
        print('Value {} found in the list at position {}'.format(random_value,i+1))
        break