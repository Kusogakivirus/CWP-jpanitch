import sys
count = 0

if len(sys.argv) - 1 != 2:
    print("none")
else:
    first = sys.argv[1]
    second = sys.argv[2]
    for i in range(len(second) - len(first) + 1):
        if second[i:i + len(first)] == first:
            count += 1
    print(count)