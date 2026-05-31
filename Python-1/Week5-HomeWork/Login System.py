password=1234
max=3
for attp in range(1,max+1):

    user = int(input(f"Enter password (attempt {attp}): "))
   
    if user == password:
     print(f"The correct password is {attp}")
     break
    else:
          print(f"Wrong password, try again")
           

          
    
       