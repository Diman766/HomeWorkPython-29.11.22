# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('Введите количество чисел  '))
feb = [0, 1]
for i in range(2, k+1):
    feb.append(feb[i-2] + feb[i-1])

negFeb = feb.copy()

for i in range(2, k + 1, 2):
    negFeb[i] = feb[i] * -1

negFeb.reverse()
negFeb.extend(feb[1:])

print(negFeb)
