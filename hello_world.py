# x = 4
# print ('x')
# print (x)
# print ("x")

# x = 2
# if x > 3:
#     print ('greater')
# if x < 3:
#     print ('smaller')
# print ('finish')

# n=5
# while n>0:
#     print (n)
#     n = n-1
# print ('Blast-Off')

# print ('hello world!')
# x = 4
# x = x+20
# print (x)

# Numeric Constants
# print (123)
# print ('123')
# print ("123")

# Multiplication
# a = 14
# b = 6
# c = a * b
# print (c)

# Division
# a = 96
# b = 8
# c = a / b
# print (c)

#Power or exponent
# a = 2
# b = 8
# c = a ** b
# print (c)

# Concatenation
# a = 'aaa'
# b = 'bbb'
# c = a + b
# print (c)

# Concatenation
# a = '123'
# b = '456'
# c = a + b
# print (c)

#User Input
# name = input('What is your name?')
# print ('Hello, how are you', name,'?')
# print ('How are you doing', name,'?')

#Convert Elevator Floors
# x = input('Enter the floor number in Europe format please')
# y = int(x)
# y = y + 1
# print ('Your US floor number is', y)

# x = input('Your name please')
# print ('Hello',x)

#Pay calculator Program
# x = input('Enter hours')
# y = input('Enter rate')
# a = float(x)
# b = float(y)
# final = a * b
# print ('Pay:',final)

#Conditional - Attempt2
# x = input('Enter the number')
# if int(x) > 3:
#     print ('Greater!')
# if int(x) < 3:
#     print ('Smaller!')
# print ('Finish')

#Just another if loop
# x = input('Enter the number')
# if int(x) > 20:
#     print('greater')
# if int(x) == 20:
#     print('Equal to 20')
# if int(x) < 20:
#     print('smaller')

#Two way decisions
# x = 1
# if x > 2:
#     print('Bigger')
# else:
#     print('Smaller')
# print('All done')

#ELIF Statement or Multi-way
# x = input('Enter the number: ')
# if int(x) > 20:
#     print('greater')
# elif int(x) == 20:
#     print('Equal to 20')
# else:
#     print('smaller')

#Try and Except Block - Error Handling
# userinput = input('Enter the number: ')
# try:
#     ppp = int(userinput)
# except:
#     ppp = -1
# if ppp > 0:
#     print ('Nice Answer!')
# else:
#     print ('Not a number!')

#Hourly rate quiz and puzzle
# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# try:
#     fh = float(sh)
#     fr = float(sr)
# except:
#     print('Error, please enter numeric input')
#     quit()
# #print(fh, fr)
# if fh > 40:
#     reg = fr * fh
#     otp = (fh - 40.0) * (fr * 0.5)
#     xp = reg + otp
# else:
#     xp = fh * fr
# print(xp)

#Week 5 second assignment scoring quiz
# x = input('Enter the score between 0.0 and 1.0')
# y = float(x)
# if y > 1.0:
#     print('Out of range!')
# elif y >= 0.9:
#     print('A')
# elif y >= 0.8:
#     print('B')
# elif y >= 0.7:
#     print('C')
# elif y >= 0.6:
#     print('AD')
# elif y < 0.6:
#     print('F')


# Functions
# Functions declaration
# def testing():
#     print ('foo')
#     print ('bar')
# # Invoking the function
# testing()

# Custom Function - Just run in an interactive mode
# def greet(lang):
#     if lang == 'en':
#         print('Hello, you are English!')
#     elif lang == 'fr':
#         print('Bonjour, you are French!')
#     else:
#         print ('Hello there!')



# Random Try
# def computepay(h,r):
#     y = h * r
#     return y

# hrs = input("Enter Hours:")
# hrs2 = float(hrs)
# rate = input("Enter Rate:")
# rate2 = float(rate)
# p = computepay(hrs2,rate2)
# print(p)

#Assignment 4.6 Functions
# sh = input("Enter Hours: ")
# sr = input("Enter Rate: ")
# try:
#     fh = float(sh)
#     fr = float(sr)
# except:
#     print('Error, please enter numeric input')
#     quit()
# #print(fh, fr)
# def computepay(fh, fr):
#     if fh > 40:
#         reg = fr * fh
#         otp = (fh - 40.0) * (fr * 0.5)
#         xp = reg + otp
#     else:
#         xp = fh * fr
#     return xp
# ppp = computepay(fh, fr)
# print (ppp)

# Infinite While Loop
# n = 5
# while n > 0:
#     print ('Lather')
#     print ('Rinse')
# print('Dry off!')

# For Loop
# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print ('Blast Off!')

# Largest Number So far program
# Largest_so_far = -1
# print ('Before' ,Largest_so_far)
# for number in [1, 5, 6, 45, 23, 85, 99, 666, 256, 951]:
#     if number > Largest_so_far:
#         Largest_so_far = number
# print ('After' ,Largest_so_far)

# Counting the elements from a loop
# count = 0
# for x in [1, 6, 2, 5, 8, 4, 55, 36, 12]:
#     count = count + 1
# print ('Total Count: ', count)

#Adding the number in a loop
# count = 0
# for x in [1, 6, 2, 5, 8, 4, 55, 36, 12]:
#     count = x + count
#     print(x, count)

# Final assignment course 1

# largest = None
# smallest = None
# while True:
#     try:
#         num = raw_input("Enter a number: ")
#         if num == "done":
#             break
# #        print (num)
#         num = int(num)
#         if largest is None or largest < num:
#             largest = num
#         elif smallest is None or smallest > num:
#              smallest = num
#     except ValueError:
#         print('Invalid input')

# print ('Maximum is',largest)
# print ('Minimum is',smallest)
