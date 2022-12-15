
def main(data):
    vis = set()

    vis.add((0, 0))

    x, y = [0] * 2, [0] * 2

    nxt = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}

    for item in data.strip().split('\n'):
        d, steps = item.split()
        for _ in range(int(steps)):
            x[-1], y[-1] = x[-1] + nxt[d][0], y[-1] + nxt[d][1]
            for k in range(2, 3):
                if abs(x[-k] - x[-k+1]) <= 1 and abs(y[-k] - y[-k+1]) <= 1:
                    continue
                if abs(x[-k] - x[-k+1]) >= 1:
                    x[-k] += 1 if (x[-k+1] - x[-k] > 0) else -1
                if abs(y[-k] - y[-k+1]) >= 1:
                    y[-k] += 1 if (y[-k+1] - y[-k] > 0) else -1
            vis.add((x[-2], y[-2]))

    return len(vis)


if __name__ == '__main__':
    with open('sample.1.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
