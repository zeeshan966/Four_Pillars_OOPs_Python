

# Polymorphism.
class Employee:
    def work(self):
        return "Base Class"

class Developer(Employee):
    def work(self):
        return "Writing Code"

class Designer(Employee):
    def work(self):
        return "Designing"

class Tester(Employee):
    def work(self):
        return "Testing"


employees = [Developer(),Designer(),Tester()]
for emp in employees:
    print(emp.work())
