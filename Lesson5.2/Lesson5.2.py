
#Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
#Для решения задачи создайте переменную и в неё положите слово с помощью input()
#А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

#5.2 - Доработать. Программа также должна выводить количество каждой гласной по отдельности.


word = (input("enter the word: ")) 
a = word.count('a') 
e = word.count('e') 
i = word.count('i') 
o = word.count('o') 
u = word.count('u') 
y = word.count('y') 

x = a + e + i + o + u + y

print("All vowels: ",x) 
print("All consonant: ",len(word)-x) 


if a == 0:
    print ("a = False")
else:
    print ("a= ", a)
    
if e == 0:
    print ("e = False")
else:
    print ("e= ", e)
    
if i == 0:
    print ("i = False")
else:
    print ("i= ", i)
    
if o == 0:
    print ("o = False")
else:
    print ("o= ", o)
    
if u == 0:
    print ("u = False")
else:
    print ("u= ", u)
    
if y == 0:
    print ("y = False")
else:
    print ("y= ", y)
