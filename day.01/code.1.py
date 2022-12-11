
def main(data):
    ans = [0]

    for num in data.strip().split('\n'):
        if num == '':
            ans.append(0)
            continue
        ans[-1] += int(num)

    return max(ans)


if __name__ == '__main__':
    with open('sample.in', 'rb') as fp:
        print(f'Sample:\n{main(fp.read().decode())}')
    with open('puzzle.in', 'rb') as fp:
        print(f'Puzzle:\n{main(fp.read().decode())}')
