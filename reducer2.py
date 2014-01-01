#!/usr/bin/python

import sys


# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

highReno = 0
highToledo = 0
highChandler = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if thisKey == "Reno":
	    if float(thisSale) > highReno:
    		highReno = float(thisSale)

    elif thisKey == "Toledo":
	    if float(thisSale) > highToledo:
    		highToledo = float(thisSale)

    elif thisKey == "Chandler":
        if float(thisSale) > highChandler:
            highChandler = float(thisSale)

print "Reno: " + str(highReno)
print "Toledo: " + str(highToledo)
print "Chandler: " + str(highChandler)
