a = int(input())

if a == 0:
    print("zero number")
elif (a <= 0) and (a % 2 == 0): 
    print ("negative even number")
elif (a >= 0) and (a % 2 == 0):    
    print ("positive even number")
else: 
    print ("the number is not even")