def compare(x, y):
    if isinstance(x, list) and isinstance(y, list):
        for sx, sy in zip(x, y):
            ans = compare(sx, sy)
            if ans == 0:
                continue
            return ans
        if len(x) == len(y):
            return 0
        if len(x) < len(y):
            return 1
        if len(x) > len(y):
            return -1

    if isinstance(x, int) and isinstance(y, int):
        if x == y:
            return 0
        if x < y:
            return 1
        if x > y:
            return -1

    if isinstance(x, int):
        return compare([x], y)
    if isinstance(y, int):
        return compare(x, [y])

    return 0


def main(data):
    ans = 0
    for i, text in enumerate(data.strip().split('\n\n'), 1):
        list0, list1 = text.split()
        list0, list1 = eval(list0), eval(list1)
        if(compare(list0, list1) == 1):
            ans += i
    return ans


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
