from main import fetch_lines

from itertools import pairwise

INPUT: str = 'd2.in'


def first() -> int:
    res = 0
    for line in fetch_lines(INPUT):
        line = [int(x) for x in line.split()]

        diff = [x - y for x, y in pairwise(line)]
        for x in diff:
            if not (1 <= abs(x) <= 3):
                break

            if x * diff[0] < 0:
                break
        else:
            res += 1
            continue

    return res


def second() -> int:
    res = 0
    for line in fetch_lines(INPUT):
        line = [int(x) for x in line.split()]

        for i in range(len(line)):
            diff = [x - y for x, y in pairwise(line[:i] + line[i + 1:])]
            for x in diff:
                if not (1 <= abs(x) <= 3):
                    break

                if x * diff[0] < 0:
                    break
            else:
                res += 1
                break

    return res


if __name__ == '__main__':
    print(first() == 660)
    print(second() == 689)
