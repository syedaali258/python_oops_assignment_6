class A:
    def show(self):
        print("Method from class A")

class B:
    def show(A):
        print("Method  from class B")

class C(A):
    def show(self):
        print("Method from class C" )

class D(B, C):
    pass


#creating an object of class D 
d = D()

#calling the show() method to observe the Method Resolution order (MRO)

#printing the MRO to observe the order
print(D.mro())