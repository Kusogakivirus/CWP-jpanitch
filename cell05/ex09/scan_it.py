#!/usr/bin/python3
import sys, re
count = 0

if (str(len(sys.argv)-1) != "2"):
    print("none")
else:
    key = sys.argv[1]
    s = sys.argv[2]
    result = re.findall(key, s)
    print(len(result))