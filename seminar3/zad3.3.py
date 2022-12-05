from random import*
numbr= int(input("количество элементов списка: "))
array=[0]* numbr
splitArray=[]
for ind in range(numbr):
    array[ind] = random()*10
print("Массив: ", array,end= " ")
mx=0
mn=10**16
for ind in range(numbr):
    splitArray.append(str(array[ind]).split('.'))
    if int(splitArray[ind][1])<mn:
        mn=int(splitArray[ind][1])
    if int(splitArray[ind][1])>mx:
        mx=int(splitArray[ind][1])
diff=mx-mn
diff="0"+"."+str(diff)
diff=float(diff)
print(diff)
