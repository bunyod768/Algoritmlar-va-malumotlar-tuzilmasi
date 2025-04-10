from datetime import datetime
import random as r
numbers = []
for i in range(100000):
    numbers.append(r.randint(1,10000))
    
def linear_search(list,item):
    start = datetime.now()
    for i in range(0,len(list)):
        if list[i] == item:
            end = datetime.now()
            return i, end - start
    end = datetime.now()   
    return None,end - start
result ,defference = linear_search(numbers,8)  
print('qiymat indeksi:',result)  
print('vaqt sarfi:',defference)
