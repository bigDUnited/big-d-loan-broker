#!/usr/bin/env python
# -*- coding: utf-8 -*-

#printline
print "Hello Python!"

#function
def fun():
	print "Java is love, JAVA IS LIFE!"
	return 2

#boolean
marek = False

#if condition
if marek:
	#print all available commands with the object
	print dir(fun)
elif marek != 1:
	#empty method body
	pass
else:
	#call function & print the return(if func without return, it will be "none")
	print fun()
	#print function address
	print fun

#inline if statement true_cond if condition else false_cond
end = True if marek == False else False

#go from 1 to 13 in increments of 2 and print with a tab - one line result
for i in range(1,14,2):
    if i == 12:
        #skip this iterations and move to the next one
        continue
    print(i,end='\t')
    if i == 14:
        #stop the loop completely
        break

#multiline strings(need \)
total = "marek " + \
		"you"

#multiline [],{},()
group = {"hey",
"you"}

print total,group

#different ways to write strings
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences.


nice"""

print word, sentence,paragraph

#comments
#hahah
print "me"#hahaha


#multiple statements on single line(separate with ;)
print "this";print "works";print "fine"

#not strongly typed(can be with the new version of python)
counter = 100          # An integer assignment
print counter
counter = 1000.0       # A floating point
print counter
counter = "Java"       # A string
print counter

#multiple variable assignment
a = b = c = 1
print a,b,c

#immutable array - if one variable changes all others assigned to it changes unless you initialize a new list with []
a = b = c = [1,2]
b.append(3)
print "Immutable array: (all should be [1,2,3])",a,b,c
b = [2,3]
print "B will have a new list:",a,b,c


a, b, c = 1, 2, "Java"
print a,b,c

# Python has five standard data types
	# Numbers
	# String
	# List
	# Tuple
	# Dictionary

str = 'Hello World!'
#string[start:end(not included):jump]
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string
print (str[-4:-2])   # Print string counting backwards from the end
print (str[::2])   # Print every second letter

#find out if substring is in string
print("Hell" in str)
print("hola" in str)


#wait for user(\n - newline)
raw_input("\n Press anything to exit.")
