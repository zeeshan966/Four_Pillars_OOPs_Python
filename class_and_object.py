
# Determine the mean of class and object using Banking System.
# Constructor.
# Abstraction.
# Encapsulation.
# Inheritance:- Access the property and Behavior child class from base class.
# Code Reusable.

class College:
    # Create a Constructor.
    def __init__(self,Roll_Number,Course,Stream):
        # Make Private Attributes.
        self.__Roll_Number=Roll_Number
        self.__Course = Course
        self.__Stream = Stream


    def get_Roll_Number(self):
        return self.__Roll_Number

    def get_course(self):
        return self.__Course

    def get_Stream(self):
        return self.__Stream


    def is_Exist(self,BoolValue):
        if(BoolValue):
            print("I am Student of this college")
        else:
            print("Student does not exist")

# Create Derived or Child Class.
class Student(College):
    # Create a Constructor. 
    def __init__(self,Student_Name,Roll_Number,Course,Stream):
        super().__init__(Roll_Number,Course,Stream)
        self.__Student_Name=Student_Name


    # Create Display Method.

    def DisplayMethod(self):
        print("----------Student Detail--------")
        print('Student Name : ',self.__Student_Name)
        print('Student Roll_Number : ',self.get_Roll_Number())
        print('Student Course : ',self.get_course())
        print('Student Stream : ',self.get_Stream())





# Inheritance with Banking System with Customer.

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

class Customer(Bank):
    # Constructor.
    def __init__(self,Customer_Name,Account_Number,IFSC_Code,Balance):
        # Active the Constructor of Parent Class.

        super().__init__(Account_Number,IFSC_Code,Balance)
        self.__Customer_Name = Customer_Name


    # Create a Method.

    def UserProfile(self):
        print("-------Customer Details-------")
        print("Customer Name : ",self.__Customer_Name)
        print("Customer Account_Number : ",self.get_Account_Number())
        print("IFSC Code : ",self.get_IFSC_Code())


# Create object of Banking System.

c1 = Customer("Zeeshan Ahmad",10011,'UPGBR',1000)
c1.Check_Balance(True)
c1.Deposit(5000)
c1.Check_Balance(True)
c1.Withdraw(1000)
c1.Check_Balance(True)
c1.UserProfile()
c1.Check_Balance(True)



# Create object of College Class.
# s1 = Student("Zeeshan Ahmad",110022,'B.Tech','CSE')
# s1.DisplayMethod()
# s1.is_Exist(False)