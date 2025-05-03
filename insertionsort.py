from datetime import datetime as dt

def insertionSort(array: list) -> list:
    start = dt.now()
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    end = dt.now()
    farq = end - start
    return array, farq

A = []
import random as rd
for i in range(1000):
    A.append(rd.randint(-100,100))
tartib, farq_vaqt = insertionSort(A)
print("insertionsort")
print(f"tartiblangan ro'yxat: {tartib}\nketgan vaqti: {farq_vaqt}")
