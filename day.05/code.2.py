
def main(data):
    stacks, moves = data.split('\n\n')
    stacks = stacks.split('\n')[::-1]
    status = [None] + [[] for _ in stacks[0].split()]
    for stack in stacks[1:]:
        for i, k in enumerate(range(1, len(stack), 4), 1):
            if stack[k] != ' ':
                status[i].append(stack[k])

    for move in moves.strip().split('\n'):
        _, a, _, b, _, c = move.split()
        a, b, c = int(a), int(b), int(c)
        status[c].extend(status[b][-a:])
        status[b] = status[b][:-a]
    return ''.join(s.pop() for s in status[1:])


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
