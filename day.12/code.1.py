
def main(data):
    heightmap = [list(r) for r in data.strip().split('\n')]

    bfs = []
    vis = set()
    for r in range(len(heightmap)):
        for c in range(len(heightmap[r])):
            if heightmap[r][c] == 'S':
                heightmap[r][c] = chr(ord('a'))
                bfs.append((r, c, 0))
                vis.add((r, c))
            if heightmap[r][c] == 'E':
                heightmap[r][c] = chr(ord('z') + 1)

    for r, c, steps in bfs:
        if heightmap[r][c] == chr(ord('z') + 1):
            return steps
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if not 0 <= nr < len(heightmap):
                continue
            if not 0 <= nc < len(heightmap[nr]):
                continue
            if (nr, nc) in vis:
                continue
            if ord(heightmap[nr][nc]) <= ord(heightmap[r][c]) + 1:
                bfs.append((nr, nc, steps + 1))
                vis.add((nr, nc))

    return False


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
