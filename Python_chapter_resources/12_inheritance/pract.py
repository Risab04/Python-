class Parent1:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        return f"Parent's name is {self.name}"

class Child(Parent1):
    def __init__(self,name,age):
        super().__init__(name)
      
        #super().__init__(name)  # Call the Parent's constructor
        self.age = age

    def show_details(self):
        return f"{super().show_name()}, and age is {self.age}"

# Create an instance of Child
child = Child("John", 25)
print(child.show_details())  # Output: Parent's name is John, and age is 25
