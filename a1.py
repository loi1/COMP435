import sys

tracker = {} # tracker = {integer value : # of appearances}
try: # read new file and get list of strings
    f = open(sys.argv[1],"r")
    lines = f.read().splitlines()
except:
    sys.exit()
for line in lines: # fill in tracker with number of appearances of each line
    num = int(line, 16) # convert each line from 16 -> 10, string -> int
    if not num in tracker: # if not in dict, add it and set value to 1, else increment value by 1
        tracker[num] = 1
    else:
        tracker[num] += 1
values = tracker.keys() # extract keys from dict so we can sort it
values.sort() # sort keys by base 10, lowest to higest
for value in values: #print the hex value of keys and its value if value >= 2
    if tracker[value] >= 2:
        print("%x" % value + ' ' + str(tracker[value])) # 'print (%x)' to convert from base-10 (int) to hex (string)
        # note: '%x' strips hex value of any trailing L's or leading 0x's
