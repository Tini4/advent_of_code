from main import fetch_lines

INPUT: str = 'd4.in'


def first() -> int:
    arr: list[list[str]] = []
    for line in fetch_lines(INPUT):
        arr.append(list(line))

    res = 0

    for i, line in enumerate(arr):
        for j, c in enumerate(line):
            if c != 'X':
                continue

            if (i + 3 < len(arr)
                    and arr[i + 1][j] == 'M' and arr[i + 2][j] == 'A' and arr[i + 3][j] == 'S'):
                res += 1

            if (i - 3 >= 0
                    and arr[i - 1][j] == 'M' and arr[i - 2][j] == 'A' and arr[i - 3][j] == 'S'):
                res += 1

            if (j + 3 < len(line)
                    and arr[i][j + 1] == 'M' and arr[i][j + 2] == 'A' and arr[i][j + 3] == 'S'):
                res += 1

            if (j - 3 >= 0
                    and arr[i][j - 1] == 'M' and arr[i][j - 2] == 'A' and arr[i][j - 3] == 'S'):
                res += 1

            if (i + 3 < len(arr) and j + 3 < len(line)
                    and arr[i + 1][j + 1] == 'M' and arr[i + 2][j + 2] == 'A' and arr[i + 3][j + 3] == 'S'):
                res += 1

            if (i - 3 >= 0 and j - 3 >= 0
                    and arr[i - 1][j - 1] == 'M' and arr[i - 2][j - 2] == 'A' and arr[i - 3][j - 3] == 'S'):
                res += 1

            if (i + 3 < len(arr) and j - 3 >= 0
                    and arr[i + 1][j - 1] == 'M' and arr[i + 2][j - 2] == 'A' and arr[i + 3][j - 3] == 'S'):
                res += 1

            if (i - 3 >= 0 and j + 3 < len(line)
                    and arr[i - 1][j + 1] == 'M' and arr[i - 2][j + 2] == 'A' and arr[i - 3][j + 3] == 'S'):
                res += 1

    return res


def second() -> int:
    arr: list[list[str]] = []
    for line in fetch_lines(INPUT):
        arr.append(list(line))

    res = 0

    for i, line in enumerate(arr):
        for j, c in enumerate(line):
            if c != 'A':
                continue

            if i + 1 < len(arr) and i - 1 >= 0 and j + 1 < len(line) and j - 1 >= 0:
                if (arr[i + 1][j + 1] == 'M' and arr[i + 1][j - 1] == 'M'
                        and arr[i - 1][j + 1] == 'S' and arr[i - 1][j - 1] == 'S'):
                    res += 1

                if (arr[i + 1][j + 1] == 'M' and arr[i + 1][j - 1] == 'S'
                        and arr[i - 1][j + 1] == 'M' and arr[i - 1][j - 1] == 'S'):
                    res += 1

                if (arr[i + 1][j + 1] == 'S' and arr[i + 1][j - 1] == 'M'
                        and arr[i - 1][j + 1] == 'S' and arr[i - 1][j - 1] == 'M'):
                    res += 1

                if (arr[i + 1][j + 1] == 'S' and arr[i + 1][j - 1] == 'S'
                        and arr[i - 1][j + 1] == 'M' and arr[i - 1][j - 1] == 'M'):
                    res += 1

    return res


if __name__ == '__main__':
    print(first() == 2633)
    print(second() == 1936)
