#del keyword
# class Student:
#     def __init__(self,name):
#         self.name = name

# s1  = Student("Anuj")
# del s1
# print(s1)
# class Account: 
#     def __init__(self,acc_no,acc_pass):
#       self.acc_no = acc_no
#       self.__acc_pass = acc_pass
#     def reset_pass(self):
#        print(self.__acc_pass)

# acc1 =  Account("123","RBI")
# print(acc1.acc_no)
# print(acc1.reset_pass())
# class Person:
#     __name = "anonymous"

#     def __hello(self):
#         print("Hello person")
#     def welcome(self):
#         self.__hello()

   
# p1 = Person()
# print(p1.welcome())


# class Car: #inheritance
#     def __init__(self,type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stop...")
# class Toyotacar(Car) :     
#     def __init__(self,name,type):
#         self.brand = name
#         super().start()
#         super().__init__(type)
# car1 = Toyotacar("Prius","electric")
# print(car1.type)

# class Fortuner(Toyotacar):
#     def __init__(self,type):
#         self.type = type
# car1 = Fortuner("Dizel")
# car1.start()
# class A:
#     varA = "wlcome to class A"
# class B:
#     varB ="welcome to class B"
# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)    
#classmethod
# class Person:
#     name ="Annpo"
#     # def changeName(self,name):
#     #     Person.name = name
#     @classmethod
#     def changeName(cls,name):
#         cls.name = name
# p1 = Person()
# p1.changeName("RAhul kumar")
# print(p1.name)
# print(Person.name)
# class  Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy+self.chem+self.math) / 3 )+"%"
   
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math) / 3 )+"%"
    

# stu1 =  Student(78,67,66)

# stu1.phy  = 33
# print(stu1.percentage)
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i+",self.img,"j")

#     def __add__(self,num2):
#         newReal =  self.real + num2.real
#         newImg = self.img +num2.img
#         return Complex(newReal,newImg)
    

#     def __sub__(self,num2):
#         newReal =  self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal,newImg)
    

# num1 = Complex(1,3)    
# num1.showNumber()

# num2 = Complex(1,9)    
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()
# Practice question
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

c1 = Circle(21)
print(c1.area())
print(c1.perimeter)


# Practice question
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("role = ",self.role)
        print("dept= ",self.dept)
        print("salary = ",self.salary)

e1 = Employee("accountant","finance",45000,)
e1.showDetails()


    # Practice question
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         super().__init__(Engineer,"IT","75000")
# eng1 = Employee("rahul",400000)
# eng1.showDetails()
  # Practice question
class Order():
    def __init__(self,item,price):
        self.item =  item
        self.price = price

    def __gt__(self,ord2):
        return self.price > ord2.price
ord1  = Order("chips",50)
ord2 = Order("blanket",8000)
print(ord1<ord2)