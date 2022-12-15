
def main(data):
    x, cycles = 1, 0
    ans = []
    for line in data.strip().split('\n'):
        if line[:4] == 'noop':
            ans.append('#' if cycles % 40 - 1 <= x <= cycles % 40 + 1 else '.')
            cycles += 1
        else:
            _, num = line.split()
            num = int(num)
            ans.append('#' if cycles % 40 - 1 <= x <= cycles % 40 + 1 else '.')
            cycles += 1
            ans.append('#' if cycles % 40 - 1 <= x <= cycles % 40 + 1 else '.')
            cycles += 1
            x += num

    ans = [''.join(ans[k:k+40]) for k in range(0, len(ans), 40)]
    ans = '\n'.join(ans)
    return ans


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
