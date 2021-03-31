def binary_search (list, target):
    first = 0
    last = len(list)-1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint]== target:
            return midpoint
        elif list[midpoint] < target :
            first = midpoint + 1
        else : 
            last = midpoint - 1
    return None

a= [x for x in range(1,11)]
print(a)
print(binary_search(a,1))




