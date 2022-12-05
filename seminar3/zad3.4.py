#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроеных методов (арифметически)
from random import*
numb=randint(0,999)
print("Десятичное число: ",numb)
binnumb=0
pozition=0
while numb>0:
    bindigit=numb%2
    binnumb+=bindigit*10**pozition
    pozition+=1
    numb//=2
print(binnumb)