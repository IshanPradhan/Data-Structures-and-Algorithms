import random

def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    mid=n // 2
    for _ in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1
    return list_of_elements

def binary_search(l,value):
    first = 0
    last = len(l) - 1
    found = False
    while(first <= last and not found):
        mid = (first + last) // 2
        if(l[mid]==value):
            found = True
            break
        else:
            if(value<l[mid]):
                last = mid - 1
            else:
                first = mid + 1

    if(found==True):
        print('Element found')
    else:
        print('Element not found')

li = initialize_list_of_elements(10)

print('Randomly Generated list is: {}\n'.format(li))

random_value = random.choice(li)

print('Random Value chosen from the list is {}\n'.format(random_value))

li.sort()           # Since we need Sorted list for bubble sort

binary_search(li,random_value)
