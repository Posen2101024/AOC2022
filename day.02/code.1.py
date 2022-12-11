
def main(data):
    scores = {
        'A X': 1 + 3,
        'A Y': 2 + 6,
        'A Z': 3 + 0,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 1 + 6,
        'C Y': 2 + 0,
        'C Z': 3 + 3,
    }

    return sum(scores[line] for line in data.strip().split('\n'))


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
