# Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)

x = int(input("enter natural number: "))
a = 1

if x < 0:
    print ("Error")
else:
    for i in range(a, int(x/2)+1): 
        if x % i == 0:
            a += 1
    print (a)
            
