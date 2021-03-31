def recursive_binary_search (list, target):
    if len(list) ==0:
        return False

    else : 
        midpoint = (len(list))//2
        
         
        if list[midpoint] == target:
            return True
        else : 
            if list[midpoint] < target:
                return recursive_binary_search (list[midpoint+1:], target)
            else : 
                return recursive_binary_search (list[:midpoint],target)



a= [x for x in range(1,11)]
print(a)
print(recursive_binary_search(a,499))


""" Read this for explanation. why we have not taken midpoint - 1 in 
second condition : 

a = [x for x in range (11)]
print(a)
print(len(a))
midpoint = len(a)//2
print(midpoint)
print(a[midpoint:])
print(a[midpoint+1:])
print(a[:midpoint])
print(a[:midpoint-1])



output of the above code is : 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
11
5
[5, 6, 7, 8, 9, 10]
[6, 7, 8, 9, 10]
[0, 1, 2, 3, 4]
[0, 1, 2, 3]

"""
