# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst = [1, 2, 3, 4, 5]

if int(((len(lst) % 2))) == 0:
    finLst = [lst[i]*lst[-i-1] for i in range(len(lst)//2)]
else:
    finLst = [lst[i]*lst[-i-1] for i in range(len(lst)//2 + 1)]
print(finLst)
