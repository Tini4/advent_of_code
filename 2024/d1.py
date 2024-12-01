from main import fetch_lines

INPUT: str = 'd1.in'


def first() -> int:
    left = []
    right = []
    for line in fetch_lines(INPUT):
        line = [int(x) for x in line.split()]

        left.append(line[0])
        right.append(line[1])

    left.sort()
    right.sort()

    res = 0
    for x, y in zip(left, right):
        res += abs(x - y)

    return res


def second() -> int:
    left = []
    right = {}
    for line in fetch_lines(INPUT):
        line = [int(x) for x in line.split()]

        left.append(line[0])

        if line[1] not in right:
            right[line[1]] = 0
        right[line[1]] += 1

    res = 0
    for x in left:
        if x not in right:
            continue

        res += x * right[x]

    return res


if __name__ == '__main__':
    print(first() == 1580061)
    print(second() == 23046913)
