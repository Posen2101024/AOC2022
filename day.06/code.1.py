
def main(data):
    for i in range(4, len(data)):
        if len(set(data[i-4:i])) == 4:
            return i


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
