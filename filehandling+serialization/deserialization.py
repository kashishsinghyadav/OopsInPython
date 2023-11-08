# file handling + serialization and deserialization

f=open('sample.txt','w')#to open the file if its not it created#
f.write('hello')#to write
f.write('\n kashish')
f.close()
f=open('sample.txt','a')# 'a' mode is appned mode which is add tha data to file without clear the previous data
f.write('\nhow are you ')
f.close()
lst=['hello\n','kaisi\n','ho\n']
f=open('sample.txt','a')
f.writelines(lst)#it is used to write the lines in  file to insert multile line in one operation
f.close()


f=open('sample.txt','r')
s=f.read()#f.read(10) it only return 10 length string
print(s)
f.close()

f=open('sample.txt','r')
s=f.readline()#f.read(10) it only return 10 length string
print(s)
f.close()

#context manager(with) - its a good idea to close a file after usage as it will free up the resourses
#it is used in place of f.close

with open('sample.txt','w') as f: # automatically close the file
    f.write('hellllllo kashish')

with open('sample.txt','r') as f:
    print(f.read())


#bigfile =['kashish' for i in range(1000)]
#with open('big.text','w') as f:
 #   f.writelines(bigfile)

#with open('big.text','r') as f:
 #   s=100
 #   while len(f.read(s))>0:
   #     print(f.read(s),end='***')
     #   f.read(s)# it loads the another 100 chunks into memory

#tell() it tell how many charcater you print and where your cursur
#seek is point the cursor anywhere in the text
with open('sample.txt','r') as f:
    print(f.read(5))
    print(f.tell())# currently where we are in text 
    f.seek(0)# it seek anwhere in the text
    print(f.tell())

with open('sample.txt','w') as f:
    f.write('hehehehehehehe')
    f.seek(0)
    f.write('U')


with open('kash.jpeg','rb') as f:#rb mean read binary
    with open('kash1.jpeg','wb') as wf:#wb to write binary data 
        wf.write(f.read())

# you can not store complex data stru in text format you can only sotre the string
#serialization means python data types to json-javascript object notaionfromat
#deserialization means converting the json into data types
import json
l=[1,2,3,4]
with open('demo.json','w') as f:
    json.dump(l,f)# dump the data 

d={
    1:'kashish',
    2:'singh',
    3:'tt'
    }

with open('demo.json','w') as f:
    json.dump(d,f)


t=(1,2,3,4,5)
with open('demo.json','a') as f:
    print()
    json.dump(t,f)



class Person:
    def __init__(self,fname,lname,age,gender):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.gender=gender
p=Person('kashish','singh',18,'f')

import json
def show(p):
    if isinstance(p,Person):
        return {'name': p.fname + ' ' + p.lname  ,'age':p.age,'gender':p.gender}
with open('demo.json','w') as f:
    json.dump(p,f,default=show,indent=4)


import json

with open('demo.json','r') as f:#deserializing
    d=json.load(f)
    print(d)



#pickling is the process to convert object into byte stream or bianry

class Per:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('hi my name is ',self.name, 'age is ',self.age)

k=Per('kakshi',19)

import pickle # store data in binary fromat 
with open('person.pkl','wb') as f:
    pickle.dump(k,f)
import pickle
with open('person.pkl','rb') as f:
    pic=pickle.load(f)

pic.display()




        








         
        
    




    



