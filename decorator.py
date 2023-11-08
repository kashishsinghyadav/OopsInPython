#decorator in a python is a function that recives as input and add some functionality to and return it
# this can happen only beacuse python function are 1st class

import time

def timer(func):
    def wrapper(*args):
        start=time.time()
        func(*args)
        print('time taken',func.__name__,time.time()-start,'secs')
    return wrapper
@timer
def hello():
    print('hello')
    time.sleep(2)

hello()
@timer
def sq(num):
    time.sleep(1)
    print(num**2)

sq(2)


def cheack(dt):

    def ow(func):
        def iw(*args):
            if type(*args)==dt:
                func(*args)
                
            else:
                return 'No'
        return iw
    return ow

@cheack(int)
def square(num):
    time.sleep(1)
    print(num**2)

square(2)
            
    




        








         
        
    




    



