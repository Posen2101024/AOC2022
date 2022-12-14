
def main(data):
    ans = 0
    for s in data.strip().split():
        s1, s2 = s[:len(s)//2], s[len(s)//2:]
        c = list(set(s1) & set(s2))[0]
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
