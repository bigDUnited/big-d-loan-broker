#!/usr/bin/python
#!/bin/bash
import sys

dummyDatabase = {
	"Dimitrii" : {
		"age" : 16,
		"gender" : "male",
		"country" : "Russia"
	},
	"Petranka" : {
		"age" : 14,
		"gender" : "female",
		"country" : "Bulgaria"
	}
}

def getPerson( name ) :
	print "You are searching for person with name : {0} " . format( name )
	#use .iteritems() on array if you want to loop through it
	for key,value in dummyDatabase.iteritems():
		print "Current elem : Key is {0} and Value is {1} " . format(key,value)
		if ( key == name ):
			return value
	print "Sorry person not found!"
	return False

if __name__ == "__main__":
	# if you call this script from the command line (the shell) it will
	# run the 'main' function
	result = getPerson(sys.argv[1])
	if result is not False:
		"Result found for name {0} : {1}" .format( sys.argv[1], result)
	else:
		"Nope"