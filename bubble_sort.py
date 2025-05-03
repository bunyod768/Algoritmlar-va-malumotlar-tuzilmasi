from datetime import datetime as dt
def bubbleSort(array: list) -> list:
    start = dt.now()
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    end = dt.now()
    deffer = end - start
    return array,deffer
A = []
import random as rd
for i in range(10000):
    A.append(rd.randint(-100,100))
tartib,farq_vaqt = bubbleSort(A)     
print("bubblesort")
print(f"tartiblangan ro'yxat:\nketgan vaqti:{farq_vaqt}")       
    

        
