#Напишите программу, которая принимает две строки
#вида “a/b” — дробь с числителем и знаменателем.
#Программа должна возвращать сумму
#и *произведение дробей. Для проверки своего
#кода используйте модуль fractions
import fractions

a = int(input('Введите числитель 1 '))
b = int(input('Введите знаменатель 1 '))
c = int(input('Введите числитель 2 '))
d = int(input('Введите знаменатель 2 '))

print(fractions.Fraction(a, b))

print(fractions.Fraction(c, d))

print(fractions.Fraction(a, b) + fractions.Fraction(c, d))

print(fractions.Fraction(a, b) * fractions.Fraction(c, d))



