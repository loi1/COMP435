import sys
import hashlib
import random
import string
def find_preimage(target, n):
    # grab input's first n bits
    target = target[:n]
    while (True):
        # generate random length 3 strings and create their digest
        msg = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(3)])
        m = hashlib.sha256()
        m.update(msg)
        msgDigest = m.digest()
        if (msgDigest[:n] == target):
            return msg
        else:
            continue
