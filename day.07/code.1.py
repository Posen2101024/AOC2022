
def main(data):
    vis = {}
    tmp = ['']
    for line in data.strip().split('\n'):
        items = line.split()
        if items[0] == '$' and items[1] == 'cd':
            if items[2] == '..':
                tmp.pop()
            else:
                tmp.append(tmp[-1] + '#' + items[2])
            continue
        if items[0].isnumeric():
            for c in tmp:
                vis[c] = vis.get(c, 0) + int(items[0])

    unused = vis['#/'] - 40000000
    ans = 0

    for v in sorted(vis.values(), reverse=True):
        if v >= unused:
            ans = v
        else:
            return ans


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
