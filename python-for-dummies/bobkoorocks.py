#!/usr/bin/python

# 1) Two string example - just like java, no ;
firstString = "Hello world"
secondString = "Python"
helloWorld = firstString + " " + secondString
print "Basic : " + helloWorld
print helloWorld
print "----------------------"
# 2) If Example + Use : like Switch in Java, format for print
x = 1;
if x == 1:
	print "X is {0}" . format(x)
print "----------------------"
# 3) Assigning to more than one variable
a, b = 3, 4
print "A is {0} and B is {1} " . format(a,b)
print "----------------------"
# 4) Lists - may contain any type of objects - "Python is a dynamically-typed language"
funkyList = []
funkyList.append(1)
funkyList.append("Milk")
funkyList.append(5.76)
for z in funkyList:
	print "For loop : Elem is {0} " . format(z)
print "----------------------"
# 5) Simple math - go for str if not format
numbers = 1 + 2 * 3 / 4.0
print "Math operators is " + str(numbers)
remainder = 11 % 3
print "Math remainder is " + str(remainder)
squared = 7 ** 2
print "Math squared is " + str(squared)
print "----------------------"
# 6) fancy array string example
simpleStuff = "My name is "
myName = "Slim Shady"
confusedList = []
confusedList.append("(what?)")
confusedList.append("(who?)")
confusedList.append("([scratches])")
confusedList.append("(huh?)")
confusedList.append("(what?)")
confusedList.append("([scratches])")
for index, value in enumerate(confusedList):
	print "{0} {1} " . format(simpleStuff, value)
	if index == 2 or index == 5:
		print myName
print "----------------------"
# 7) List joins
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print all_numbers
# 8) Another way of formatting strings
dimitrii = "Dimitrii"
print "Heloy its, %s!" % dimitrii
print "----------------------"
# 8.1) Exercise You will need to write a format string which prints out the data using the following syntax:
# Hello John Doe. You are 23 years old. Your current balance is 53.44$.
name =  "John Doe"
age = 23
balance = 53.43999
print "Hello %s. You are %d years old. Your currentbalance is %.2f$." % (name, age, balance)
print "Name length of {0} is {1} where index of h is {2}" . format(name, len(name), name.index("h"))
for name in ["Losi","Ovchi Drun"]:
	print name
print "----------------------"
# 9) If else statements with IS operator and WHILE and icrementation
pumba = "Pumbaaaa"
count = 0;
print "----------------------"
while (count < 3):
	if count == 1:
		pumba = "sexy"
	elif count == 2:
		pumba = "else"

	if pumba is "Pumbaaaa":
		print "sexy"
	elif pumba is "sexy":
		print "pumba"
	else:
		print "Johnny la gente esta muy loca"
	count += 1
print "----------------------"
# 10) The not operator - java !
print (not False) == (False) # Prints out False
print (True) == (not False)
print "----------------------"
# 11) Print range of numbers - lolz
for x in xrange(3): # or range(5)
    print x
print "----------------------"
# 12) functions
def helloWorld():
    print "Vot u dy meeeen?"
helloWorld()
print "----------------------"
# 13) Args
def presentYourself(name, age):
	print "Hello I am %s, my age is %d :) " % (name,age)
presentYourself("Telbot", 17)
print "----------------------"
# 14) Returns
def getSum(a, b):
	return a + b
print "sum is {0} " . format(getSum(1,2))
print "----------------------"
# 15) Classes
class Galin:
	song = "Vse napred vse napred"

	def function(self):
		print "Trugvai ot tuk {0} " . format(self.song)

myObject = Galin()
print myObject.function()
print "----------------------"
# 15.1) Classes
class Namespace: pass
def ex7():
    ns = Namespace()
    ns.var = 'foo'
    def inner():
        ns.var = 'bar'
        print 'inside inner, ns.var is ', ns.var
    print 'inside outer function, ns.var is ', ns.var
    inner()
ex7()
print "----------------------"
# 16) Cool arrays
coolarray = {
	"Boyko" : "cool",
	"Teo" : 22,
	"Marek" : "stupid",
	"Martin" : "bored"
}
for key, value in coolarray.iteritems():
	print "{0} is {1}" . format(key, value)
print "----------------------"
del coolarray["Martin"]
for key, value in coolarray.iteritems():
	print "{0} is {1}" . format(key, value)
print "----------------------"
coolarray.pop("Boyko")
for key, value in coolarray.iteritems():
	print "{0} is {1}" . format(key, value)
print "----------------------"
import urllib2
response = urllib2.urlopen("https://github.com/bigDUnited")
html = response.read()
print html