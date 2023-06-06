#!/usr/bin/python3
for i in range(0, 8):
    for x in range(1, 10):
        if i < x and i != x:
            print("{}{}, ".format(i, x), end='')
print(89)
