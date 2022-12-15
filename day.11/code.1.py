class Monkey:
    def __init__(self, text):
        lines = text.split('\n')
        self.starting_items = list(map(int, lines[1][len('  Starting items: '):].split(', ')))
        self.operation = lambda old: eval(lines[2][len('  Operation: new ='):]) // 3
        true = int(lines[4][len('    If true: throw to monkey '):])
        false = int(lines[5][len('    If false: throw to monkey'):])
        self.test = lambda old: true if self.operation(old) % int(lines[3][len('  Test: divisible by '):]) == 0 else false


def main(data):
    monkeys = [Monkey(text) for text in data.split('\n\n')]

    worry_levels = [monkey.starting_items for monkey in monkeys]
    times = [0 for _ in monkeys]

    for _ in range(20):
        for i, worry_level in enumerate(worry_levels):
            monkey = monkeys[i]
            for num in worry_level:
                times[i] += 1
                worry_levels[monkey.test(num)].append(monkey.operation(num))
            worry_levels[i] = []

    return sorted(times)[-1] * sorted(times)[-2]


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
