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
