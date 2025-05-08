class  atm:
    bank_name = "HDFC Bank ATM"
    user_name = "Vishal Deshmukh"
    account_no = 220221730500 
    s_pin = 2222
    Total_Bal = 10000
    deposite = 0
    withdrawal = 0

    print(f"Wellcome to HDFC Bank ATM ")

    def __init__(self,create_pin):
        # print(f"Wellcome to {self.bank_name} ")
        self.create_pin = create_pin
        
    def Enter_your_Pin(self):
        if self.create_pin == 2222: 
            
            self.kay = int(input("Enter for 0 is check balance \n1 is deposite \n2 is withdrawal \nplease enter any one :- "))

            if self.kay == 1:
                self.deposite = int(input("Enter your deposite amount :- "))
                print(f"Your Rs.{self.deposite} deposite is successfully !")
                print(f"User Name :- {self.user_name}")
                print(f"Account No. :- {self.account_no}")
                print(f"Available Balance :- {self.Total_Bal + self.deposite - self.withdrawal }")



            
            if self.kay == 2:
                self.withdrawal = int(input("Enter your withdrawal amount More Than Rs.500 :- "))
                if self.withdrawal >= 500:
                    print(f"Your Rs.{self.withdrawal} withdrawal successfully!")
                    print("Please collect your cash..")
                    print(f"Available Balance :- {self.Total_Bal + self.deposite - self.withdrawal }")
                    if self.withdrawal < self.Total_Bal:
                        print(f"User Name :- {self.user_name}")
                        print(f"Account No. :- {self.account_no}")
                    else:
                        print(f"Your account balance can't cover the full amount check balance and try again. ")
                else:
                    print("Please Enter more than Rs.500 !")
            
            # else:
            #     print(f"Please enter 0 is check balance and 1 is depoite and 2 is withdrawal You entered {self.kay} This is wrong kay Plase try again...")


            if self.kay == 0:
                print(f"Available Balance :- {self.Total_Bal + self.deposite - self.withdrawal }")
                print(f"User Name :- {self.user_name}")
                print(f"Account No. :- {self.account_no}")
                
        
            print(f"Thank you for visiting {self.bank_name}")
        else:
            print("Wrong Pin Please try agin...")
                    
    
        

atm1 = atm(create_pin = int(input("Enter Your Four digit pin :- "))) 
atm1.Enter_your_Pin()