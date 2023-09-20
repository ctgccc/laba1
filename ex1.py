number = int(input("Введите натуральное число: "))
prev_digit = 10
is_ordered = True

while number > 0:
    digit = number % 10
    if digit > prev_digit:
        is_ordered = False
        break
    prev_digit = digit
    number //= 10

if is_ordered:
    print("Последовательность цифр упорядочена по убыванию")
else:
    print("Последовательность цифр не упорядочена по убыванию")
