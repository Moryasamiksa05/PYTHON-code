# class Student:
#     #default constructor
    #  collge_name =  "VBSPU"
#     name = "AMIT" #class attributes
#     def __init__(self,name,marks):#parametrized constructor
#         self.name = name #object attribute>>Precedence high
#         self.marks = marks
#         print("adding new student in database") 
#     name = "samiksha"  

# s1 = Student("karan",78)
# print(s1.name,s1.marks)
# s2 = Student("aman",88)
# print(s2.name,s2.collge_name)
# class Student:
#     college_name ="abc"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student",self.name)
#     def get_marks(self):
#         return self.marks

# s1= Student("amit",77)
# print(s1.name)
# s1.welcome()
# print(s1.get_marks())
  
#practice question
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("Hi",self.name,"Your avg score is :",sum/5)

# s1 = Student("karan",[90,89,56,54,100])

# s1.get_avg()
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#        self.clutch:bool
#        self.acc = True
#        print("car started..")

# car1 = Car()
# car1.start()
#practice question
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited") 
        print("Total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credited")
        print("Total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance
        

acc1 = Account(100000,12345)
print(acc1.balance,acc1.account_no)
acc1.debit(20000)
acc1.credit(10000)

acc1.credit(400000)

