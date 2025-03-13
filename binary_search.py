# royxat tartiblangan bolishi kerak!
nums = [1,2,4,6,8,10,24]
def binary_search(list,item):
    L = 0
    H = len(nums) - 1
    while L <= H :
        M = (L + H)//2
        if item < list[M]:
            H = M - 1
        if item > list[M]:
            L = M + 1
        if item == list[M]:
            return M 

    return None

print(binary_search(nums,10))


