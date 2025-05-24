class InvalidAgeError(Exception):
    def __init__(self, message = "Age must be 18 or older"):
        super().__init__(self.message)

#function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. you must be 18 or older.")
    else:
        print(f"Age {age} is valid")


# handling the excption using try.. except
try:
    age = int(input("Enter your age"))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error:  {e}")
except ValueError:
    print("please enter a valid integer age")