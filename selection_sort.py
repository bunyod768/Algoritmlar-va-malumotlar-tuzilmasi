from datetime import datetime as dt

def selectionSort(array: list) -> list:
    start = dt.now()
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    end = dt.now()
    farq = end - start
    return array, farq

# Misol uchun
A = []
import random as rd
for i in range(1000):
    A.append(rd.randint(-100,100))
tartib, farq_vaqt = selectionSort(A)
print("selectionsort") 
print(f"tartiblangan ro'yxat: {tartib}\nketgan vaqti: {farq_vaqt}")
