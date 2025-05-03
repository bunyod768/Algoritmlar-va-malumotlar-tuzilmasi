from datetime import datetime as dt

def quickSort(arr):
    start = dt.now()

    def quick(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            less = [x for x in arr[1:] if x <= pivot]
            greater = [x for x in arr[1:] if x > pivot]
            return quick(less) + [pivot] + quick(greater)

    sorted_array = quick(arr)
    end = dt.now()
    farq = end - start
    return farq

# Misol uchun
A = []
import random as rd
for i in range(1000000):
    A.append(rd.randint(-10000,10000))
farq_vaqt = quickSort(A)
print("quick sort")
print(f"tartiblangan ro'yxat: \nketgan vaqti: {farq_vaqt}")
