﻿#В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. 
#Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N чисел - перевернутый массив.

# 8.1 - Доработать. Ограничение на элементы массива не соответствует условию задания.


n = int(input())
res = []

if  (n >= 1) and (n <= 10000):
    for i in range(n):
        a = int(input())
        if a < 100000:   
            res.append(a)
            
    res.reverse()    
    print(res)
    
else:
    print("Error")




