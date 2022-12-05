from random import*
numbr= int(input("количество элементов списка: "))
lowbound= int(input("нижняя граница значений: "))
uppbound= int(input("верхняя граница значений: "))
array=[0]* numbr
for ind in range(numbr):
    #print(array[ind],end=" ")
    array[ind] = randint(lowbound,uppbound)
print("Массив: ", array,end= " ")
sumElem = 0
print("нечетные элементы: ", end=" ")
for ind in range(1,numbr,2):
    print( array[ind], end=" ")
    sumElem+=array[ind]
print("ответ: ",sumElem)
