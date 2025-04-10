from datetime import datetime
import random as r
# royxat tartiblangan bolishi kerak!
nums = []
for i in range(0,100001):
    nums.append(r.randint(1,10000))

def binary_search(list,item):
    start = datetime.now()
    L = 0
    H = len(nums) - 1
    while L <= H :
        M = (L + H)//2
        if item < list[M]:
            H = M - 1
        if item > list[M]:
            L = M + 1
        if item == list[M]:
            end = datetime.now()
            return M,end - start
    end = datetime.now()
    return None,end - start

result,defference = binary_search(nums,10)
print('qiymat indeksi:',result)
print('ishlatilgan vaqt:',defference)

