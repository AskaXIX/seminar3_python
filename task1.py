# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3 Output:  [4, 5, 1, 2, 3]


from random import randint

print(lst := [randint(-5, 5) for _ in range(10)])

shift = int(input("Insert number to shift: "))

# print(lst[-shift:] + lst[:-shift])

# с помощью срезы
for i in range(shift):
    lst.insert(0, lst.pop())
print(lst)

# с помощью индекса
new_list = []
for i in range(100):
    print(lst[i%len(lst)])
