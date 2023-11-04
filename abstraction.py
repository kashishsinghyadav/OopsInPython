# what is abstraction ?

# abstraction is an iThe concept allows us to hide the implementation from the user but shows only essential information to the user. Using the concept developer can easily make changes and added over time.


# There are the following advantages of abstraction:

# It reduces complexity.
# It avoids delicacy.
# Eases the burden of maintenance
# Increase security and confidentially.

from abc import ABC,abstractmethod # abstarct class contain at least one abstact method which is define in another inherited class and also we cannot create the object of abstract class

class Bankdata(ABC):
    def database(self):
        print('connected to databse')
    @abstractmethod 
    def secure(self):
        pass

class Webdata(Bankdata):
    def App(self):
        print('app connected')
    
    def secure(self):
        print('this is secure')

object = Webdata()
object.App()
object.secure()
