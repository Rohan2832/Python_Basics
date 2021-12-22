# game = input("enter your game: ")

# if game.lower() == "calculator":
#     def func():
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         operation = input("Enter Calculator Operation: ")
#         if operation.lower() == "sum":
#             sum = num1 + num2
#             print(sum)
#         elif operation.lower() == "diff":
#             diff = num1 - num2
#             print(diff)
#         elif operation.lower() == "product":
#             product = num1 * num2
#             print(product) 
#         elif operation.lower() == "quotient":
#             quotient = num1 /num2 
#             print(quotient)
#         elif operation.lower() == "remainder":
#             remainder = num1 % num2
#             print(remainder)
#         else:
#             print("Don't know that operation: ")
#     func()
# elif game.lower() == "chess":
#     print("LMAO get lost")
# else:
#     print("Don't know that game, check with someone else: ")


# i = 0
# evenList = []
# oddList = []
# while i in range(0,101):
#     if i % 2 == 0:
#         print(f"{i} is even")
#         evenList.append(i)
#     else:
#         print(i)
#         oddList.append(i)
#     i += 1
# print(i)
# print(evenList)
# print(oddList)



# primeList =[]
# nonPrimeList = []
# universalList = []

# for number in range(1,101):
#     if number == 1:
#         universalList.append(number)
#         print(f"Universal List is: {universalList}")
#     elif number > 1:
#         for divisor in range(2,number):
#             if number % divisor != 0:
#                 primeList.append(number)
                
#             else:
#                 nonPrimeList.append(number)
#             break
   
# print(f"Prime numbers list is {primeList}")
# print(f"Composite numbers list is {nonPrimeList}")



#### ---- FizzBuzz List:
fizzList = []
buzzList = []
fizzbuzzList = []
numList =[]

i = 0
while i in range(0,101):
    if i % 3 == 0 and i % 5 !=0:
        fizzList.append(i)
    elif i % 5 == 0 and i % 3 != 0:
        buzzList.append(i)
    elif i % 3 == 0 and i % 5 == 0:
        fizzbuzzList.append(i)
    else:
        numList.append(i)
    i+=1

print(f"Fizz numbers are: {fizzList}")
print(f"Buzz numbers are: {buzzList}")
print(f"FizzBuzz numbers are: {fizzbuzzList}")
print(f"Other numbers are: {numList}")




                














    
    




