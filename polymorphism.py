# The word polymorphism is derived from the two words i.e. ploy and morphs. Poly means many and morphs means forms. It allows us to create methods with the same name but different method signatures. It allows the developer to create clean, sensible, readable, and resilient code.

class Polymorphism: # method overloaing / static binding 
    def expre(self,name=None):#method overloaing is achive using default paramter or keyword parameter
        if name is not None:
            print('my name is ' + name)

        else:
            print('name is not given')
obj = Polymorphism()
obj.expre()
obj.expre('kashish')

class Overriding:
    def display(self):
        print('hello')

class B(Overriding):
    def display(self):
        super().display()
        print('hii')

obj=B()
obj.display()
        
