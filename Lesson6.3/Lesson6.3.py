# Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные числа на заданном отрезке через пробел.

a = int(input())
b = int(input())

if a <= b:
    for x in range(a, b + 1):
        if x % 2 == 0:
            print(x, end = " ")
else:
    print("Error")