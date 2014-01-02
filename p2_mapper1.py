#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.split()
    if len(data) == 10:
        ip, identity, user, date, timezone, mathod, path, protocol, status, size = data
        print"{0}\t{1}".format(path, ip)
