def bubbleSort(a):
    for _ in range(0,len(a)-1):
        swapped = False
        for j in range(0,len(a)-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                swapped = True
        if(swapped == False):
            break
    return a

li = [67,34,8,22,23,-1,6,7,18]
print('List before sorting: {}'.format(li))
sorted_li = bubbleSort(li)
print('List after sorting: {}'.format(sorted_li))