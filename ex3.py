n = int(input("Введите количество элементов в списке: "))
print("Введите элементы списка: \n")
a = [int(input()) for i in range(n)]
s = 0

for i in range(n):
   if a[i] > 0:
       s += a[i]
print("1)Сумма элементов списка:", s)

''''
sum_after_zero = 0
zero_encountered = False
for i in range(n):
   if a[i] == 0:
       zero_encountered = True
   elif zero_encountered:
       sum_after_zero += a[i]
       if zero_encountered:
           print("Сумма элементов после первого нуля:", sum_after_zero)
       else:
           print("Сумму посчитать нельзя")
'''''

if 0 in a:
    print("2)Сумма элементов после первого нуля:",sum(a[a.index(0):]))
else:
    print("2)Сумму посчитать нельзя, так как нет в списке нет 0")

positive_numbers = []
for i in range(n):
    if a[i] >= 0:
        positive_numbers.append(a[i])
print("Список с положительными числами:", positive_numbers)