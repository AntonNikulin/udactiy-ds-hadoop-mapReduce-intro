#!/usr/bin/python

import sys


# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
totalValue = 0
numberSales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    numberSales += 1
    totalValue += float(thisSale)

print "Number of Sales: " + str(numberSales)
print "Total Value of Sales: " + str(totalValue)
