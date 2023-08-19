
word = (input("enter the word: ")) 
a = word.count('a') 
e = word.count('e') 
i = word.count('i') 
o = word.count('o') 
u = word.count('u') 
y = word.count('y') 
if (a == 0) or (e == 0) or (i == 0) or (o == 0) or (u == 0):
    print("False") 
else:
    print(f"vowels: {a + e + i + o + u}") 
    print(f"consonant: {len(word) - (a + e + i + o + u)}")
