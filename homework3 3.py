from itertools import count
import random
numbers = int(input("Введите количество элементов списка : "))
list = [None] * numbers
list2 = [None] * numbers
countt = 0
for i in range(len(list)):
    list[i] = float(input())
    list2[i] = round(list[i] % 1,2)
print(f"Разница между максимальным и минимальным значением дробной части элементов равна :  {round(max(list2) - min(list2), 3)}")



