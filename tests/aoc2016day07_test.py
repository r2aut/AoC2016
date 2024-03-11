""" Day 7: Internet Protocol Version 7 unit tests """

from src.aoc2016day07 import scan_line_for_tls
from src.aoc2016day07 import scan_line_for_ssl

test_str_TLS = list()
test_str_TLS.append("abba[mnop]qrst")
test_str_TLS.append("abcd[bddb]xyyx")
test_str_TLS.append("aaaa[qwer]tyui")
test_str_TLS.append("ioxxoj[asdfgh]zxcvbn")


def test_scan_line_for_tls():
    """ scan_line_for_tls unit test """
    counter = 0
    for line in test_str_TLS:
        if scan_line_for_tls(line):
            counter += 1
    assert counter == 2

test_str_SSL = list()
test_str_SSL = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""".split("\n")

def test_scan_line_for_ssl():
    """ scan_line_for_ssl unit test """
    counter = 0
    for line in test_str_SSL:
        if scan_line_for_ssl(line):
            counter += 1
    assert counter == 3
