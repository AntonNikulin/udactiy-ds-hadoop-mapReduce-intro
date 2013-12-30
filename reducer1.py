#!/usr/bin/python
 
import sys
 
toysTotal = 0
elTotal = 0
for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
	# Something wrong. Skip
		continue
 
	thisKey, thisSale = data_mapped
 
	if thisKey == "Toys":
		toysTotal += float(thisSale)
 
	if thisKey == "Consumer Electronics":
		elTotal += float(thisSale)
 
print "Toys: " + str(toysTotal)
print "Consumer electronics: " + str(elTotal)