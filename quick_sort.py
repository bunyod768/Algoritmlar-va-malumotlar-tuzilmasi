from random import randrange
A = [1,100,50,30,500,350,150,500]

def qsort(array):
    if len(array) < 2:
        return array
    else:
         
         pivot = array.pop(randrange(len(array)))       
         kichik = [i for i in array if i <= pivot]
         katta = [ i for i in array if i > pivot]

         return qsort(kichik) + [pivot] + qsort(katta)

print(A)
print(qsort(A))




