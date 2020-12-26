#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import md5


def mining(secret, prefix):
    i = 1
    while True:
        if md5(
            (secret + str(i)).encode("utf-8")).hexdigest().startswith(prefix):
            break
        i += 1
    print("Answer to {}: {}".format(prefix, i))


if __name__ == '__main__':
    mining("ckczppom", "00000")
    mining("ckczppom", "000000")
