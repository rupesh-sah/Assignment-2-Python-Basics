
                #Assignment-2: Python Basics

#(Q.1) Write a python script to add comments and print “Learning Python” on screen.
# Ans -->
#print("Learning Python")

'''(Q.2) Write a python script to add multi line comments and print values of four variables,
each in a new line. Variable contains any values.'''
# Ans -->
'''var1 = "moniter"
var2 = "cpu"
var3 = "motherboard"
var4 = "mouse"

print(var1, var2, var3, var4,)'''

'''(Q.3)Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “MySirG”,5.46, 3+4j, etc)'''
# Ans -->

var1 = 35
var2 = True
var3 = "MySirG"
var4 = 5.46
var5 = 3+4j

print(var1, var2, var3, var4, var5)

'''(Q.4)Write a python script to print the id of two variables containing the same integer
values.'''
# Ans -->

a = 10
b = 10
print(a is b)
    #or
print(a,b)

'''(Q.5)Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable'''
# Ans -->

#(Q.6)Write a python script to print all the keywords
# Ans -->
key = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(key)
# (Q.7)On Python shell use help() function and display the list of keywords
# Ans -->
import keyword
print("Python keywords are...")
print(keyword.kwlist)

#(Q9)Name the keywords, used as data in the Python script.
#Ans -->
# (if , elif , and else)

'''(Q.10)Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)'''
from datetime import date

today = date.today()
print("Today's date:", today)