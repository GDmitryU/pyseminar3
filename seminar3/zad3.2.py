from random import*
numbr= int(input("количество элементов списка: "))
lowbound= int(input("нижняя граница значений: "))
uppbound= int(input("верхняя граница значений: "))
array=[0]* numbr
sumArray=[]
for ind in range(numbr):
    array[ind] = randint(lowbound,uppbound)
print("Массив: ", array)
for ind in range((numbr+1)//2):
        sumArray.append(array[ind]+array[numbr-1-ind])
print("Суммы: ",sumArray)

