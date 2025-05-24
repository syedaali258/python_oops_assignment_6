class Multiplier:
    def __init__(self, factor):
        self.factor = factor  #setting the factor

    def __call__(self, number):
        #Thus method allows the object to be  called like a function
       return number * self .factor 
    
# creating an instance of Multiplier with a favtor of 5
multilpier = Multiplier(5)

# Testing with callable() to check if the object is callable
print(callable(multilpier))

# calling the object like a function to multiply an input by the factor
result = multilpier(10)
print(result)
