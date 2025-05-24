#step1: parent class 
class Person:
    def __init__(self, name):
        self.name = name

#step2: child class
class Teacher(Person): #inheriting person
   def __init__(self, name, subject):
       super().__init__(name)
       self.subject = subject

   def display(self):
       print(f"Name:{self.name}, Subject: {self.subject}")

if __name__ == "__main__":
    teacher = Teacher("Meerab" , "English")
    teacher.display()