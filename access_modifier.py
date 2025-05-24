class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

if __name__ == "__main__":
    emp = Employee("Asad", 50000, "123-45-6789")

    #access public variable
    print("public variable:",  emp.name)
    #access protected variable
    print("protected variable:" , emp._salary)
    #access private variable
    try :
      print("private variable:" , emp.__ssn)
    except AttributeError:
        print("cannnot access private variable __ssn.")

    


    
    

