import sys
sys.path.append("src")

import io

from T07_Internet_Protocol_Version_7 import scanLineForTLS
from T07_Internet_Protocol_Version_7 import scanLineForSSL

test_str_TLS = list()
test_str_TLS.append("abba[mnop]qrst")
test_str_TLS.append("abcd[bddb]xyyx")
test_str_TLS.append("aaaa[qwer]tyui")
test_str_TLS.append("ioxxoj[asdfgh]zxcvbn")


def test_scanLineForTLS():
    counter = 0
    for line in test_str_TLS:
        if scanLineForTLS(line):
            counter += 1
    assert counter == 2

test_str_SSL = list()
test_str_SSL = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""".split("\n")

def test_scanLineForSSL():
    counter = 0
    for line in test_str_SSL:
        if scanLineForSSL(line):
            counter += 1
    assert counter == 3
