class ATM:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()


    def menu(self):
        while(True):
            user_input=input("""
                 Hello ! welcome to this ATM.please enter:-
                 1. to create pin
                 2. to deposit
                 3. to withdraw
                 4. to check balance
                """)


            if user_input=="1":
                create_pin(self)
            elif user_input=="2":
                deposit(self)
            elif user_input == "3":
                withdraw(self)
            elif user_input == "4":
                check_balance(self)
            elif user_input == "5":
                check_pin(self)
            else:
                break


def create_pin(self):
    self.pin = input()
    print("pin created succesfully")
def deposit(self):
    temp = input("enter your pin")
    if temp==self.pin:
        self.balance = self.balance + int(input("enter amount"))
        print("deposit succesfully")
    else:
        print("wrong pin")

def withdraw(self):
    temp = input("enter your pin")
    if temp == self.pin:
        amount = int(input("enter amount to withdraw"))
        if amount < self.balance:
            self.balance = self.balance - amount
            print("withdraw succesfully")
        else:
            print("balance is less")
    else:
        print("wrong pin")

def check_balance(self):
    print(f"total balance : {self.balance}")

def check_pin(self):
    print(f"your pin : {self.pin}")


hdfc=ATM()










