# The concept allows us to inherit or acquire the properties of an existing class (parent class) into a newly created class (child class). It is known as inheritance. It provides code reusability.

# single level inheritance

class M:
    def fun(self):
        print('this is parent class constructor')

class Beta(M): 
    def fun(self):
        super().fun()
        print('this is base class construtor')

obj1 =Beta()
obj1.fun()

# multilevel 

class A:
    def __init__(self):
        print('hii')
    def display1(self):
        print('parent class')
class B(A):
    def __init__(self):
        
        print('hello')

    def display(self):
        super().display1()
        print('parent parent')

class C(B):
    def __init__(self):
        print('hey')
    def display(self):
        print('Base')

ob=C()
C.display()

#multiple inheritamce

class A:
    def display(self):
        print('this is parent class')
    
class B:
    def display1(self):
        print('this is second class')

class C(A,B):
    def  display3(self):
        print('this is child class')

obj=C()
C.display3()
