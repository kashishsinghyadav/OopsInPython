class Atm:
    def __init__(self):#constructor
        self.__pin=""
        self.__bal=0
        self.menu()
 

    def menu(self):
        user_input=input("""
        enter the button
        1. create pin
        2.check balance
        3.deposit
        4.withdraw
        5.to exit
        
        """)

        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.cheack_balance
            
        elif user_input=='3':
            self.dposit()
        elif user_input=='4':
            self.withdraw()
        else:
            print('bye')
    def create_pin(self):
        self.__pin=input('enter your pin')
        print('pin create successfully')
    def dposit(self):
        temp=input('enter your pin')
        if temp==self.__pin:
            amt=int(input('enter amount'))
            self.__bal=self.__bal+amt
        else:
            print('invalid pin')
    def withdraw(self):
        temp=input('enter your pin')
        if temp==self.__pin:
            amt=int(input('enter the amount'))
            if amt<self.__bal:
                self.__bal=self.__bal-amt
                print('poeration sucessful')
            else:
                print('amount is not avilable')
        else:
            print('invalid pin')
    def cheack_balance(self):
        temp=input('enter your pin')
        if temp==self.__pin:
            print(self.__bal)
        else:
            print('incorrect')
            


a=Atm()







        
        

