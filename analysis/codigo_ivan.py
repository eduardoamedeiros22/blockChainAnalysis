import numpy as np
import time
import random


def main():
    PERM = 10000
    b = np.load('../resources/block_integer_array.npy')
    ONEMONTH = int(len(b) / 12)
    ini = time.time()
    for e in range(12):
        print(e, ':')
        START = int(e * ONEMONTH)
        perm = [x for x in b[START:START + ONEMONTH]]
        ref = countSeq(perm)
        c = [0] * 100
        for i in range(PERM):
            random.shuffle(perm)
            p = countSeq(perm)
            for _c in range(100):
                if p[_c] < ref[_c]:
                    c[_c] += 1
        for i in range(len(c)):
            if c[i] >= int(PERM * 0.95):
                print(i, c[i])


def countSeq(blocks):
    prev = -1
    count= [0]*100
    for _b in blocks:
        if _b==prev:
            count[_b]+=1
        prev = _b
    return count


if __name__ == "__main__":
    main()