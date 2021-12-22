# print("hello World")
# age = 20
# print(age)

# name = input("Enter patient name: ")
# age = int(input("Enter age: "))
# # print("welcome Mr.",name, "aged", age, "years old")
# print(f"Welcome Mr {name} aged {age} years old")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# sum = num1 + num2
# print("Sum is: ",sum)

# weight = int(input("Enter your weight: "))
# units = input("Enter Kg or lbs: ")

# if units == "Kg":
#     weight *= 2.205
#     print("your weight in pounds is: ",weight, "lbs")

# elif units == "lbs":
#     weight /= 2.205
#     print("your weight is: ",weight, "Kgs")
# else:
#     print("wrong units")


# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# def greet(first_name,last_name):
#     print("Hello", first_name, last_name)

# Name = greet(first_name,last_name)
# print(Name)


#FIZZ BUZZ PROBLEM
# num = int(input("Enter your number: "))
# def FizzBuzz(num):
#     if num % 3 == 0 and num % 5 !=0:
#         print("Fizz")
#     elif num % 5 == 0 and num %3 !=0:
#         print("Buzz")
#     elif num % 3 == 0 and num %5 == 0:
#         print("Fizzbuzz")
#     else:
#         print("Your number is ",num)
# FizzBuzz(num)


#CLASSES AND INHERITANCE
# name = input("enter your name: ")
# language = input("what language do you speak?: ")

# class Person:
#     def __init__(self,name,language):
#         self.name = name
#         self.language = language
#         print("Hello", name, "you speak", language)

# answer = Person(name,language)
# print(answer)


#### ---- string1 start = string2 end (LETTERS): 

# string1 = input("enter first string: ")
# string2 = input("enter second string: ")
# def common():
#     if string1[0].lower() == string2[-1].lower():
#         return True
#     else:
#         return False

# answer = common()
# print(answer)



#### ---- string1 start = string2 end (Words):
# string1 = input("Enter your first string: ")
# string2 = input("Enter your second string: ")
# string1Final = str.split(string1)
# string2Final = str.split(string2)
# def common(object):
#     if string1Final[0].lower() == string2Final[-1].lower():
#         return True
#     else:
#         return False
# answer = common(object)
# print(answer)



#### ---- Interchange first half with second half b/w 2 strings
# a = "warrior"
# b = "fighter"
# la = len(a)
# lb = len(b)
# def swapHalves(a,b):
#     c = a[0:la//2] + b[lb//2:lb]
#     print(c)
#     d = b[0:lb//2] + a[la//2 : la]
#     print(d)
# swapHalves(a,b)
# e = input("enter another word: ")
# d = input("enter it's switch partner: ")
# swapHalves(e,d)


# def hospDeets(name,age,problem):
#     print(f"Hello {name}.")
#     print(f"I see you're {age} years old.")
#     print(f"The doctor will look into your {problem} soon!")

# hospDeets("Jon",21,"Flu")
# hospDeets("Ro",22,"Chlamydia")
# hospDeets("Jay",16,"AIDS")

   
#### ---- FizzBuzz 1-100
# i = 1
# while i in range(1,100):
#     if i % 3 == 0 and i % 5 !=0:
#         print("Fizz")
#     elif i % 5 == 0 and i %3 !=0:
#         print("Buzz")
#     elif i % 3 == 0 and i %5 == 0:
#         print("Fizzbuzz")
#     else: 
#         print(i)
#     i+=1
# print(i)


# car_name = input("Which car would you like to buy: ")
# price = int(input("How much are you willing to spend?: "))
# class Car:
#     def __init__(self,car_name,price):
#         self.car_name = car_name
#         self.price = price

#     def judgeCar(car_name):
#         if car_name.lower() == "ferrari" or car_name.lower() == "Lamborghini" or car_name.lower() == "tesla":
#             print(f"LMAOOO you can't afford no {car_name}")
#         else:
#             print(f"Nice! good luck with your {car_name}")

#     judgeCar(car_name)

#     def judgePrice(price):
#         if price > 1000000:
#             print(f"Wait, what? {price}??\nLMAOOO you can't afford that")
#         else:
#             print(f"{price} Rupees is a good deal though!")

#     judgePrice(price)

# ans = Car(car_name,price)
# print(ans)



#### ---- Reverse a list
# a = [1,2,5,6,8,9]
# print(a)
# print(a[::-1])
# b = ["cat", "dog", "frog"]
# print(b)
# print(b[::-1])

# a = list(str.split(input("Enter your list elements: ")))
# print(f"your list is: {a[::-1]}")

# b = input("enter your numbers: ")
# number_list = list(map(int,b.split()))
# print(f"So your integers in reverse are: {number_list[::-1]}")



####---- MIDPOINTS ON A LIST: 
# a = list(str.split(input("Enter list element: ")))
# midpoint = a[len(a) // 2]
# print(midpoint)

# b = input("enter list numbers: ")
# number_list = list(map(int,b.split()))
# midpoint = number_list[len(number_list) // 2]
# print(midpoint)

####---- MEan of list
# num = input("enter your list numbers: ")
# num_list = list(map(int,num.split()))

# for num in num_list:
#     meanOfList = sum(num_list)/len(num_list)
# print(meanOfList)



####---- append list to another list
# a = [1,2,3,4,5,6]
# b = [7,8,9,10,11]

# for element in b:
#     a.append(element)

# print(a)


# a = [1,2,3,4,5,6]
# b = [7,8,9,10,11]

# for element in b:
#     a.append(element)

# def meanOfList(a):
#     mean = sum(a)//len(a)
#     print(mean)
# meanOfList(a)

a = list(input("enter your sentence: "))
i = ["a","e","i","o","u"]
def hasVowels(a):
    for i in a:
        if i in a:
            print(a not in i)
        else:
            print(i)
ans = hasVowels(a)
print(ans)

####---- Dictionaries
# phone = {"one": 1, "two" : 2, "three": 3,"Four": 4}
# # print(phone["one"])
# phone.update("won")
# print(phone)


