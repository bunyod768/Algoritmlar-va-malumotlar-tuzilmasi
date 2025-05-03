from datetime import datetime as dt

def mergeSort(array: list) -> list:
    start = dt.now()

    def merge(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            merge(left)
            merge(right)

            i = j = k = 0

            # Ikkala bo'lakni solishtirib, birlashtirish
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            # Qolgan elementlarni qo'shish
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    merge(array)
    end = dt.now()
    farq = end - start
    return array, farq

# Misol uchun
A = []
import random as rd
for i in range(1000000):
    A.append(rd.randint(-100,100))
tartib, farq_vaqt = mergeSort(A)
print("merge sort")
print(f"tartiblangan ro'yxat:\nketgan vaqti: {farq_vaqt}")
