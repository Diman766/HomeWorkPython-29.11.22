# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(0, len(lst)-1):
    if type(lst[i]) == int:
        lst.pop(i)
lst = [str(lst[i]) for i in range(0, len(lst))]

lstResult = []

for i in range(0, len(lst)):
    tmp = lst[i].split('.')
    lstResult.append((tmp[1]))

lstResult = ['0.' + lstResult[i] for i in range(0, len(lstResult))]
lstResult = [float(lstResult[i]) for i in range(0, len(lstResult))]
   
print(max(lstResult) - min(lstResult))
