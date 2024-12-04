from main import fetch_lines

import re
from itertools import pairwise

INPUT: str = 'd3.in'


def first() -> int:
    res = 0
    for line in fetch_lines(INPUT):
        for m in re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', line):
            res += int(m[0])*int(m[1])

    return res


def second() -> int:
    res = 0
    enabled = True
    for line in fetch_lines(INPUT):
        for m in re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)|(don\'t\(\))|(do\(\))', line):
            if m[3]:
                enabled = True
                continue

            if m[2]:
                enabled = False
                continue

            if enabled:
                res += int(m[0]) * int(m[1])

    return res


if __name__ == '__main__':
    print(first())
    print(second())
