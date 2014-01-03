#!/usr/bin/python

import sys

hitsTotal = 0
oldKey = None

maxHits = 0
maxPath = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        if hitsTotal > maxHits:
            maxHits = hitsTotal
            maxPath = oldKey
        oldKey = thisKey;
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += 1

#Process the last key
if oldKey != None:
    if hitsTotal > maxHits:
        maxHits = hitsTotal
        maxPath = oldKey

print maxHits
print maxPath
