number = int(input("Введите число : "))
list = [None] * (number * 2 + 1)
start = 1
second = 1
list[number] = 0
list[number + 1] = 1
list[number + 2] = 1
i = 1
k = number + 3
while i < (number - 1)  :
    start = start + second
    list[k] = start
    k += 1
    i += 1
    if i >= (number - 1):
        break
    second = start + second
    list[k] = second
    k += 1
    i += 1
    if i >= (number - 1):
        break
i = 1
while i <= number:
    list[number - i] = list[number + i]
    i += 1
    if i > (number ):
        break
    list[number - i] = -list[number + i]
    i += 1
    if i > (number ):
        break
print(list)









exit()
def fibonnahci(n):
    if n == 1 or n == 2:
        return 1
    return fibonnahci(n - 1) + fibonnahci(n - 2)
print(fibonnahci(number))
