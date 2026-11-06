
# Encapsulation.


# Abstraction.

class Bank:
    # Constructor.
    def __init__(self,Account_Number,IFSC_Code,Balance):

        #  Private Data Members.

        self.__Account_Number=Account_Number
        self.__IFSC_Code=IFSC_Code
        self.__Balance=Balance

    def get_Account_Number(self):
        return self.__Account_Number

    def get_IFSC_Code(self):
        return self.__IFSC_Code

    def get_Balance(self):
        return self.__Balance

    # Show Customer Balance.

    def Check_Balance(self,BoolDetail):
        if(BoolDetail):

            print('Customer Balance is: ',self.get_Balance())

        else:
            print("User does not exist")

    def Deposit(self,amount):

        if(amount>0):

            
            self.__Balance+=amount
            print('₹',amount,": Deposited Successfully")

        else:
            print("Negative Amount will not be accepted")

    def Withdraw(self,amount):
        if(amount>0 and amount<self.__Balance):

            
            self.__Balance-=amount
            print('₹',amount,": Withdraw Successfully")

        else:
            print("Negative amount will not be accepted and withdraw amount should be less current balance")


c1 = Bank("Zeeshan Ahmad","UPGBR",2000)
c1.Check_Balance(True)
c1.Deposit(10000)
c1.Check_Balance(True)
c1.Withdraw(2000)
c1.Check_Balance(True)