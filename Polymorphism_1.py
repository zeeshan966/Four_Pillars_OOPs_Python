# Polymorphism.

class PunjabBank:
    # method 1.
    def deposit(self):
        return "Amount Deposited Successfully(PunjabBank)"
    def withdraw(self):
        return "Amount withdraw successfully(PunjabBank)"

class UttarPradeshGraminBank(PunjabBank):
    def deposit(self):
        return "Amount Deposited Successfully(UttarPradeshGraminBank)"
    def withdraw(self):
         return "Amount withdraw successfully(UttarPradeshGraminBank)"


class StateBank(PunjabBank):
    def deposit(self):
        return "Amount Deposited Successfully(StateBank)"
    def withdraw(self):
        return "Amount withdraw successfully(StateBank)"

bankcall = [UttarPradeshGraminBank(),StateBank(),PunjabBank()]
for bank in bankcall:
    print(bank.deposit())
    print(bank.withdraw())