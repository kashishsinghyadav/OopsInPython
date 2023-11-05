#Aggregation (has a relationship)
#_classname__methodname/variablename that is used to access privete variable

class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    

    def print_add(self):
        print(self.address.get_city(),self.address.pin,self.address.state)

    def edit_profile(self,new_name,new_city,new_pin,new_state):
         self.name=new_name
         self.address.edit_add(new_city,new_pin,new_state)
class Address:
    def __init__(self,city,pin,state):
        self.__city=city
        self.pin=pin
        self.state=state
    def get_city(self):
        return self.__city
    def edit_add(self,new_city,new_pin,new_state):
        self.__city=new_city
        self.pin=new_pin
        self.state=new_state


add1=Address('kanpur',208017,'up')

obj=Customer('kashish','f',add1)
obj.print_add()
obj.edit_profile('kashish','pune',2020,'maha')
obj.print_add()







