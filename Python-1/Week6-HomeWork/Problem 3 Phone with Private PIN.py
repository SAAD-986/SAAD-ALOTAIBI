
class Phone:
    def __init__(self, owner, pin):
        self.owner = owner     
        self.__pin = pin       
    def unlock(self, attempt):
        if attempt == self.__pin:
            print("Phone unlocked!")
        else:
            print("Wrong PIN")           
phone = Phone("Saad", "1234")
phone.unlock("1234")    
phone.unlock("110")  
