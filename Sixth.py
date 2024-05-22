#Functions
# a = 5
# b = 5
# sum = a+ b
# print(a+b)
# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# calc_sum(1,5)

# def sum(c,b):
#     return c+b
# sum1 =sum(38,67)
# print(sum1)

# def print_hello():
#     print("hello")
#     print_hello()
# Avg of three numbers
# def cal_avg(a,b):
#     sum = a+b
#     avg = sum / 2
#     print(avg)
#     return avg
# cal_avg(668,677)
# print("samiksha",end=" ")
# print("maurya")

# User defined function

# def cal_prod(a,b=3):
#     print(a*b)
#     return a *b
# cal_prod(6)
# Practice que1
# cities = ["jaunpur","delhi","noida","pune","mumbai","chennai"]
# # def print_len(cities):
# #     print(len(cities))
# # print_len(cities)
# def print_list():
#     for item in list:
#         print(item,end =" ")

# print_list(cities)
# Factorial number practice question
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)

# def cal_fac(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact*=i
#         print(fact)
# cal_fac(17)
# def convertor(usd_val):
#     inr_val = usd_val *83
#     print(usd_val,"USD=",inr_val,"INR")
# convertor(17000)
# Recursion
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)
# Recursion
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))
# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1) + n
# sum =  cal_sum(5)
# print(sum)
list =  ["sam","mau","rau","jau","haow"]
def print_list(list, idx=0):
    if(idx==len(list)):
          return
          print(list[0])
    print_list(list, idx+1)
print_list(list)



