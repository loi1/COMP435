import sys
import hashlib

def hammingdistance(hex1, hex2):
    if isinstance(hex1, basestring) == False or isinstance(hex2, basestring) == False:
        sys.exit()
    count = 0
    a = hex1
    b = hex2
    # turn hex string into binary string, cut off first 2 char '0b'
    a = bin(int(a, 16))[2:]
    b = bin(int(b, 16))[2:]
    # turn bin str into lists so we can change their size and compare
    a = list(a)
    b = list(b)
    # contingency case: add zeros to shorter bin numbers so they match lengths so we can compare them
    if len(a) > len(b):
        for i in range(len(a)-len(b)):
            b.insert(i,'0')
    elif len(a) < len(b):
        for i in range(len(b)-len(a)):
            b.insert(i,'0')
    # iterate thru each element and count differences in bits
    for j in range(len(a)):
        if a[j] != b[j]:
            count += 1
    return count
