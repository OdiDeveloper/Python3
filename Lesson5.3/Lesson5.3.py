
Invest = int(input("Invest: ")) 
Mike   = int(input("Mike: "))
Ivan   = int(input("Ivan: "))

if (Mike >= Invest) and (Ivan >= Invest):
    print (2)
elif (Mike >= Invest) and (Ivan < Invest):
    print ("Mike")
elif (Mike <= Invest) and (Ivan >= Invest):
    print ("Ivan") 
elif Mike + Ivan >= Invest:
    print (1)
else:
    print (0)
    
 