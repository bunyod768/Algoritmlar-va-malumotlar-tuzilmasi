
numbers = [2,-1,4,3,5,8,-100,14]
def linear_search(list,item):
    for i in range(0,len(list)):
        if list[i] == item:
            return i
    return None
print(linear_search(numbers,8))    
