
def main(data):
    status = [list(map(int, list(r))) for r in data.strip().split('\n')]
    lr, lc = len(status), len(status[0])

    ans = 0

    for r in range(1, lr-1):
        for c in range(1, lc-1):
            trees = []
            see = 0
            for k in range(1,lr):
                if r + k >= lr:
                    break
                see += 1
                if status[r][c] <= status[r+k][c]:
                    break
            trees.append(see)
            see = 0
            for k in range(1,lr):
                if r - k < 0:
                    break
                see += 1
                if status[r][c] <= status[r-k][c]:
                    break
            trees.append(see)
            see = 0
            for k in range(1,lc):
                if c + k >= lc:
                    break
                see += 1
                if status[r][c] <= status[r][c+k]:
                    break
            trees.append(see)
            see = 0
            for k in range(1,lc):
                if c - k < 0:
                    break
                see += 1
                if status[r][c] <= status[r][c-k]:
                    break
            trees.append(see)

            if trees[0]*trees[1]*trees[2]*trees[3] > ans:
                ans = trees[0]*trees[1]*trees[2]*trees[3]

    return ans


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
