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
elif marek == 1:
	#empty method body
	pass
else: 
	#call function & print the return(if func without return, it will be "none")
	print fun()
	#print function address
	print fun
	
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


#wait for user(\n - newline)
raw_input("\n Press anything to exit.")
