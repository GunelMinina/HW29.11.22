# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input('Введите количество чисел: '))
some_list = []
for _ in range (0, n):
    some_list.append(float(input('Введите число: ')))

max_num = 0
min_num = 1

for i in some_list:
    if max_num < (i % 1):
        max_num = (i % 1)
    if  min_num > (i % 1)  and (i % 1 != 0):
        min_num = (i % 1)
       
print(max_num - min_num)