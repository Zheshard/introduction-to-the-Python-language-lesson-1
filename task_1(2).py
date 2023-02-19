# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

strNumber = input('Введите трехзначное число: ', )

if (len(strNumber) != 3):
    print('Введено неверное число!')
else:
    number = int(strNumber)
    sumDigit = number//100 + number % 100//10 + number % 10
    print(sumDigit)
