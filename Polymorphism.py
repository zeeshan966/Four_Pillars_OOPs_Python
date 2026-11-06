
# When a child class defines a method with the exact same name as a method in its parent class, it overrides the parent’s implementation. This allows you to call the same method signature on a collection of diverse objects and achieve distinct results at runtime.

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
