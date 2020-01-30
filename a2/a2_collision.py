import sys
import hashlib
import random
import string

def find_collision(n):
    # use num since we're checking the first n*2 digits of hex digest (hex is twice as long as regular digest)
    tracker = {}
    num = n*2
    while (True):
        # generate random strings and hash hex digests
        msg = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(1,32)])
        m = hashlib.sha256()
        m.update(msg)
        msgDigest = m.hexdigest()
        # if digest is already in map, check if its msg is same as current one; if yes, continue, or if not, create the tuple
        if msgDigest[:num] not in tracker:
            tracker[msgDigest[:num]] = msg
        else:
            if msg == tracker.get(msgDigest[:num]):
                continue
            else:
                return tracker.get(msgDigest[:num]), msg
