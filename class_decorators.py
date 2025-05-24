#class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from decorator!"
    
    #Add the greet method to the class 
    cls.greet = greet
    return cls

#Applying the class decorator to the person class 
@add_greeting
class person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, i am {self.name}")

# creating an instance of the person class 
person = person("Bushra")

#calling the greet method added by the decorator
print(person.greet())

    
