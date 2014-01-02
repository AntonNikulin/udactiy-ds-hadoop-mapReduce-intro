#!/usr/bin/python

import sys


totalHitsPage = 0
totalIP = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisPath, thisIP = data_mapped
    if thisPath == "/assets/js/the-associates.js":
        totalHitsPage += 1
    if thisIP == "10.99.99.186":
        totalIP += 1

print "Hits to path: " + str(totalHitsPage)
print "Hits by IP: " + str(totalIP)
