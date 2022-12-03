# # class employes:#class name
# #     qualification="b tech"

# #     def __init__(self,x,y,z):#instance attributes
# #         self.name=x
# #         self.age=y
# #         self.sex=z

# #     def employee_details(self) : #method attributes
# #         print(self.name,self.age,self.sex,'these are details') 

# # emp1=employes('ramesh', 35, 'M') #instantiating employes class
# # emp2=employes('vijay',35,'M')          
# # emp3=employes('Sanni',33,'M')


# # emp1.employee_details()
# # emp2.employee_details()
# # emp3.employee_details()


# # print("He is a {}  graduate".format(emp1.__class__.qualification))#accesing the class attribute
# # print("he is a",(emp1.__class__.qualification), "graduat")

# # print("his name is  {} and his age is   {} ".format(emp1.name,emp1.age))
# # print(emp1.name,emp1.age) #accessing the instance attribute
# # print("his name is",emp2.name)
# # print(emp1.age)
# # print(emp1.sex)



# # How to initialize constructor of Base Class
# # Base Class aka Parent Class
# class Person():
#     def __init__(self, name):
#         self.name = name 

#     def displayName(self):
#         print(self.name) 

#     # By default we can say that particular perosn is unemployed
#     def isEmployed(self):
#         print(self.name," is Un-Employed !!")

# class_name=Person("ramesh")
# class_name.displayName()
# class_name.isEmployed()

# # Derived Class aka Child Class
# class Employee(Person):

#     def __init__(self,emp_name, id_num, salary, designation):
#         self.idnumber = id_num
#         self.emp_salary = salary
#         self.emp_designation = designation

#         # Calling constructor of Base Class
#         # Person.__init__(self,emp_name)
#         super().__init__(emp_name)
        
#     def isEmployed(self):
#         print(self.name," is Employed !!")

#     def employeeDetails(self):
#         print("Employee Id is ",self.idnumber,
#         " Employee Salary is ",self.emp_salary,
#         " Employee Designation is ",self.emp_designation)

# emp1 = Employee('Shashank',5432,1000,'Data Engineer - 3')
# emp1.displayName()
# emp1.isEmployed()
# print(emp1.name)
# print(emp1.emp_salary)
# emp1.employeeDetails()




# class Computer:
#     def printing(self):
#         print("Hi iam Ramesh")


# comp1=Computer()    #print(type(comp1)  we get its class type
# Computer.printing(comp1) # typical method of calling 'printing' method
# comp1.printing() # normal method of calling a method




# class Computer:  
#     def printing(self): #creating method
#         print("Hi iam Ramesh")
#         # print("i5, Ryzen, 16 gb")


# comp1=Computer()    # creating a object  - print(type(comp1)  we get its class type
# comp2=Computer()
# # Computer.printing(comp1) # typical method of calling 'printing' method
# comp1.printing() # normal method of calling a method
# comp2.printing()




class Computer: 
    print("iam a Computer")
    count=0

    def __init__(self,mk,pcr,gen,st):
        print("Iam declaring the specifications of a computer")
        # print(Computer.count)
        
        self.make=mk
        self.processor=pcr
        self.generation=gen
        self.storage=st
        Computer.count+=1
    
    def printing(self):
        print("Hi iam printing Ramesh")
        print("make:",self.make,"Processor :",self.processor,"Generation :",self.generation,"storage: ",self.storage)
    
    def compare(self,c3):
        if self.storage==c3.storage:
            print('Their storages are equal')
        else:
            print('Their storages are not equal')   


    def update(self):
        self.generation='i9'   
        print('The updated version is : ',self.generation)
              

    def totalcount(self):
        print("Total Count=",Computer.count)



comp1=Computer('HP','Ryzen','i5','8')    #creating object
comp2=Computer('Dell','intel','i7','16')
comp3=Computer('Asus','intel','i5','8')

Computer.printing(comp1)
comp2.printing()
comp3.printing()

comp1.compare(comp3)

# comp2.compare(comp1)


print(comp3.make)
print(comp1.storage)

comp1.storage=32
comp1.processor='Atom'
print(comp1.storage)
print(comp1.processor)

comp1.update()
print(comp1.generation)

if comp1.storage==comp2.storage:
    print("comp1 and comp2 have same storage capacity")
else:
        print("comp1 and comp2 dont have same storage capacity")  

print(Computer.count)#calling total count without creating function

Computer.totalcount(comp3)
comp3.totalcount()