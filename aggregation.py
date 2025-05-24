class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee


    def show_employee(self):
        print(f"Employee in department: {self.employee.name}")

if __name__ == "__main__":
    emp =  Employee("Bushra")
    dept =  Department(emp)
    dept.show_employee()