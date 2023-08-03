from random import randint

list_1 = [randint(0, 15) for i in range(1, 7)]
print(list_1)
sorted_list = sorted(list_1)
print(sorted_list)
count = list_1.count(1)
print(count)

k = int(input("k: "))

res1 = 0
res2 = 0
for _ in sorted_list:
    if _ <= k:
        res1 = _
    if _ >= k:
        res2 = _

if k - res1 == res2 - k:
    print(res2)
elif k - res1 < res2 - k:
    print(res1)
elif res2 == 0:
    print(res1)
else:
    print(res2) 