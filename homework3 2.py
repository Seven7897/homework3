numbers = int(input("Задайте количество элементов списка : "))
list = [None] * numbers
len_list2 = int(numbers / 2)
if (numbers % 2 == 0 ):
    summ_list = [None] * len_list2
    for i in range(len(list)):
        list[i] = int(input(f"введите элемент списка с индексом - {i} : "))
    print(list)
    i = 0
    while i < len_list2 :
        summ_list[i] = int(list[i] * list[len(list) - i - 1])
        i += 1
else:
    len_list2 += 1
    summ_list = [None] * len_list2 
    for i in range(len(list)):
        list[i] = int(input(f"введите элемент списка с индексом - {i} : "))
    print(list)
    i = 0
    while i < len_list2  :
        summ_list[i] = int(list[i] * list[len(list) - i - 1])
        i += 1
print(summ_list)