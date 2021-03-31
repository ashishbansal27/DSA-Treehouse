#primary assumption for this binary search is that the 
#list should be sorted already. 

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

#summary of above code : 
#two variables named first and last to indicate the starting and ending point 
#of the list. 

# the while loop would run till the first value is less than or equal to last
# then we update the values of first and last. 

a= [x for x in range(1,11)]
print(a)
print(binary_search(a,1))




