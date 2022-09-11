numbers = int(input("Задайте количество элементов списка : "))
list = [None] * numbers
for i in range(len(list)):
    list[i] = int(input(f"Заполните элемент списка с индексом {i} : "))
len_list2 = int(numbers / 2)
list2 = [None] * len_list2
i = 1
k = 0
while i < numbers:
    list2[k] = list[i]
    k += 1
    i += 2
print(list2)
