import sys

if len(sys.argv) < 3:
    print("none")
else:
    for i in sys.argv[:0:-1]:
        print(i)