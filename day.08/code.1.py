
def main(data):
    status = [list(map(int, list(r))) for r in data.strip().split('\n')]
    lr, lc = len(status), len(status[0])

    ans = [[0] * lc for _ in range(lr)]

    for r in range(lr):
        tmp = -1
        for c in range(lc):
            if tmp < status[r][c]:
                tmp = status[r][c]
                ans[r][c] = 1
        tmp = -1
        for c in range(lc)[::-1]:
            if tmp < status[r][c]:
                tmp = status[r][c]
                ans[r][c] = 1

    for c in range(lc):
        tmp = -1
        for r in range(lr):
            if tmp < status[r][c]:
                tmp = status[r][c]
                ans[r][c] = 1
        tmp = -1
        for r in range(lr)[::-1]:
            if tmp < status[r][c]:
                tmp = status[r][c]
                ans[r][c] = 1

    return sum(sum(r) for r in ans)


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
