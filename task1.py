# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [1, 2, 3, 4, 5]
lstSum = 0

for i in range(1, len(lst), 2):
    lstSum += lst[i] 
print(lstSum)