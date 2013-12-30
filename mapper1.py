#!/usr/bin/python
 
import sys


#expected string example:
# 2013-10-09\t13:22\tMiami\tBoots\t99.95\tVisa
for line in sys.stdin:
	data = line.strip().split("\t")
	#6 tokens in correct string
	if len(data) == 6: 
		date, time, store, item, cost, payment = data
		print "{0}\t{1}".format(item, cost)