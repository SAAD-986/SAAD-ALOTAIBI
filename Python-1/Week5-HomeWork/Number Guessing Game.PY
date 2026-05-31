number = 50
num1=0
while num1 != number: 
 num1 = int (input("Gueses the number: "))
 if num1 < number:
   print ("Two low")
 elif num1 > number:
   
   print("To High")
 else:
    print("Correct the number was 50")
 break
    