
#���� ����� �� ��������� ��������� ����. ������� ��� ��������� � ������� ����? �������� �������� ����� �a�, �e�, �i�, �o�, �u�.
#��� ������� ������ �������� ���������� � � �� �������� ����� � ������� input()
#� ����� ���������� ���������� ������ �� ���� ������� ���� ���� �����-�� �� ������������� ���� ��� - �������� False

#5.2 - ����������. ��������� ����� ������ �������� ���������� ������ ������� �� �����������.


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
