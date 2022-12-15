
def main(data):
    x, cycles = 1, 0
    ans = 0
    for line in data.strip().split('\n'):
        if line[:4] == 'noop':
            cycles += 1
            if (cycles + 20) % 40 == 0:
                ans += x * cycles
        else:
            _, num = line.split()
            num = int(num)
            cycles += 1
            if (cycles + 20) % 40 == 0:
                ans += x * cycles
            cycles += 1
            if (cycles + 20) % 40 == 0:
                ans += x * cycles
            x += num
    return ans


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
