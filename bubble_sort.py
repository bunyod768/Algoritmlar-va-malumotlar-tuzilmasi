def bubbleSort(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(array)
A = [1,5,9,2,13,14,2,4,100]
bubbleSort(A)            
    

        
