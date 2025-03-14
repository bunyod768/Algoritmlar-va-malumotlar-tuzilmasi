narxlar = [1000,500,350,200,1500] # $
sorted = []
#selection sort algoritm


while narxlar:
    Max = narxlar[0]
    for i in narxlar:
       if Max < i:
           Max = i
    sorted.append(Max)
    narxlar.remove(Max)   
    

print("Saralangan narxlar",sorted) #checked