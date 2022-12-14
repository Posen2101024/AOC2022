
def main(data):
    ans = 0
    for s in data.strip().split():
        l, r = s.split(',')
        lx, ly = map(int, l.split('-'))
        rx, ry = map(int, r.split('-'))
        if lx <= rx <= ry <= ly or rx <= lx <= ly <= ry:
            ans += 1
    return ans


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
