#Lists in Python
# marks = [70,1,45,78,45,200]
# print(type(marks))
# print(marks)
# print(marks[4])
# print(len(marks))
# student = ["samiksha",20,"jaunpur"]
# print(student)
# print(student[0])
# print(student[1:2])
# age = [1,6,9,3,4,6,7,5]
# print(age[1:4])
# print(age[-4:-1])
#Tuples in Python
# tuple = (2,3,3,4,5,6,7,8,0)
# print(type(tuple))
# print(tuple[1])
# tup =(20,)
# print(tup)
# print(tuple.index(3))
# print(type(tup))
#Practice question
# a = input("Enter first fav movie: ")
# b = input("Enter second fav movie: ")
# c = input("Enter third fav movie: ")
# list = [a,b,c]
# print(list)
#Practice question 2
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 =  list1.copy()
copy_list1.reverse()
 
if(copy_list1 == list):
    print("Palindrome")
else:
    print("Not Palindrome")