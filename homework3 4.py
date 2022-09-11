import math
number = int(input("Введите число : "))
number_2 = number 
count = 0
while (number >= 1):
    number = int(math.floor(number / 2 )) 
    count += 1
list = [None] * count
i = 0
print()
while (number_2 >= 1):
    if (number_2 % 2 == 0):
        list[i] = "0"
    else: 
        list[i] = "1"
    number_2 = int(math.floor(number_2 / 2 )) 
    i += 1
if count % 2 != 0:
    count += 1 
temp = 0
i = 0
while i < count / 2:
    temp = list[i]
    list[i] = list[len(list) - i - 1]
    list[len(list) - i - 1] = temp
    i += 1
list = "".join(list)
print(list)

