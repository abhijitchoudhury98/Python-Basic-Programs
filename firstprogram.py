# a=float("5")
# b=4
# print(a+b)
# print(type(a))

# typecasting
# a=str("5")
# b=a
# print(a+b)
# print(type(a))

# ---input in python
# # name=input("Enter your name: ")
# # print("Hello", name)


# #--- add two numbers
# a = int(input("Enter First Number: "))  # if i dont mention data type i.e int , it will give the output in string format. 
# b = int(input("Enter Second Number: "))

# sum = a + b 
# print("The sum of two numbers is: ", sum)


# #Program to input side of a square & print area of square
# side = float(input("Enter the side of Square:"))
# area = side ** 2 #this is same as side*side
# print("The Area of Square is:", area)



#Program to input two floating point numbers & print their average

# num1 = float(input("Enter First Number: "))
# num2 = float(input("Enter Second Number: "))

# avg = (num1 + num2) / 2
# print("The Average of two numbers is: ", avg)



#Program to input two int numbers a and b, Print true if a is greater than or equal to b, else print false
# a = float(input("Enter your First number:"))
# b = float(input("Enter your Second number:"))

# print(a>=b)

 
# str = " Abhi ."
# str1 = str[0:4]
# print(str1)


#Program to input a string and print the length of the string
# Name = input("Enter Your Name:----")
# print("Length of Name is --",len(Name))

#Program to input a string and print the number of times a specific character appears in the string 
# str = "Abhi$@gmail.com"
# print(str.count("$"))

# Conditional Statement


# age = int(input("Enter your Age:"))
# if (age>= 18):
#     print("You are eligible to vote")
# else : 
#     print("You are not eligible to vote")


# Test = str(input("Enter Your Gender :"))
# if (Test == "Male"):
#     print("You are eligible for the Test")
# elif (Test == "Female"): 
#     print("You are not eligible for the Test")
# else :
#     print("----X----")



# num1 = 12
# num2 = 9
# Mul= num1*num2
# print("THe Multiplication of two no's are--", Mul)

# age = 26
# if(age>=18):
#     print(True)
# else:
#     print(False)

# Marks =int(input("Enter Your Marks: ")) 
# if (Marks >= 90 and Marks<100):
#     Grade = "A"
# elif (Marks>= 80 and Marks< 90):
#     Grade = "B"
# elif (Marks>= 70 and Marks< 80):
#     Grade = "C" 
# elif (Marks <70):
#     Grade = "D"
# else:
#     print("Invalid Marks Entry")

# print("Grade Of The Students: ",Grade)
   


# Program to check if a number entered by user is odd or even

# num = int(input("Enter a number: "))

# if (num % 2 ==0):
#     print(num, "is Even")
# else:
#     print(num, "is Odd",)


# WAP to find the greatest of three numbers entered by user

# num1 = int(input("Enter First Number: "))
# num2 = int(input("Enter Second Number: "))
# num3 = int(input("Enter Third Number: "))

# if (num1 > num2) and (num1 > num3):
#     print(num1, "is the greatest number")
# elif (num2 > num1) and (num2 > num3):
#     print(num2, "is the greatest number")
# else:
#     print(num3, "is the greatest number")




# Program to check if a number is a multiple of 7 or not
# num=int(input("Enter a number:"))
# if (num % 7==0):
#     print(num, "is a multiple of 7")
# else:
#     print(num, "is not a multiple of 7")



# list = [6,3,7,4,5,6,]
# list.insert(5,2)
# print(list)


# tup = (2,5,6,3,2,1)
# print(tup[1:4])
# print(tup.count(6))



#WAP to ask the user to enter names of their 3 favourite movies & store them in a list

# movies = []
# mov1 = input("1st Movie :")
# mov2 = input("2nd Movie :")
# mov3 = input("3rd Movie :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)


#WAP to check if a list is palindrome or not
# LIST = []
# fir = input("Enter your first number")
# sec = input("Enter your second number")
# trd = input("Enter your third number")

# LIST.append(fir)
# LIST.append(sec)
# LIST.append(trd)

# copy_list1 = LIST.copy()
# copy_list1.reverse()

# if(copy_list1 == LIST):
#     print("Palindrome")
# else:
#     print("Not Palindrome ")


Grade = ("C", "D","A","A","B","B","A")
print(Grade.count("A"))


list = ["C", "D","A","A","B","B","A"]
print(list.sort())
print(list)















