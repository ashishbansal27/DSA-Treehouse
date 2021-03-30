def linear_search(list, target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return None




#alt solution 

def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


a= [x for x in range(1,5)]
print(a)
print(linear_search(a,9))
