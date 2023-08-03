# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

from random import randint

list_1 = [randint(0, 10) for i in range(1, 7)]
print(list_1)

count = 0
for i in range(len(list_1)-1):
    if list_1[i+1] > list_1[i]:
        count += 1

print(count)