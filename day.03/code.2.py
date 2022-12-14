
def main(data):
    ans = 0
    lines = data.strip().split()
    for i in range(0, len(lines), 3):
        c = list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))[0]
        if ord('a') <= ord(c) <= ord('z'):
            ans += ord(c) - ord('a') + 1
        else:
            ans += ord(c) - ord('A') + 1 + 26
    return ans


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
