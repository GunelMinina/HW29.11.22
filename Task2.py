# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Введите количество чисел: '))
some_list = []
for _ in range (0, n):
    some_list.append(int(input('Введите число: ')))

index = 0
Mult_list = []
while index <= (n-1)//2 :
    Mult_list.append(some_list[index] * some_list[n-1-index])
    index += 1
print(Mult_list)