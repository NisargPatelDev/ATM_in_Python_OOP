class Atm:
    
    def __init__(self):

        self.pin = ""
        self.balance = 0

        self.menu()

    def menu(self):
        print("""
            Hello, How would you like to proceed?
            1.Enter 1 to crate PIN
            2.Enter 2 to deposite
            3.Enter 3 to withdraw
            4.Enter 4 to check balance
            5.Enter 5 to exitx
        """)

        selected = input("Enter the option Number :- ")

        if selected == "1":
           self.create_pin()
        elif selected == "2":
              self.deposite()
        elif selected == "3":
              self.withdraw()
        elif selected == "4":
              self.check_balance()
        else :
             print("bye")


    def create_pin(self):
        self.pin = input("Enter Pin :")
        print("New Pin set Successfull!")
        self.menu()

    def withdraw(self):
        if self.pin == input("Enter Your PIN :- "):
            wihtdraw_amount = int(input("Enter the amoutn you want to withdraw"))
            if wihtdraw_amount < self.balance:
                self.balance -= wihtdraw_amount
                print("Withdraw Successfull!")
                self.menu()
            else:
                print("Insufficent fun!")
                self.menu()
               
        else:
            print("Invalid PIN")
            self.menu()
            

    def deposite(self):
        if self.pin == input("Enter Your PIN :- "):
            self.balance = self.balance + int(input("Enter the amount you want to deposite : "))
            print("Deposite Succkessfull!")
            self.menu()
        else:
            print("Invalid PIN!")
            self.menu()
            

    def check_balance(self):
        if self.pin == input("Enter Your PIN :- "):
            print(f"Current Balance is :- {self.balance}")
            self.menu()
        else:
            print("Invalid Pin!")
            self.menu()
            
sbi = Atm()