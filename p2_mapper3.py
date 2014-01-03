#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.split()
    if len(data) == 10:
        ip, identity, user, date, timezone, mathod, path, protocol, status, size = data
        #No path needed. Only filename.
        print"{0}\t{1}".format(path.split("/")[-1], ip)
