def simulate(cups):
    print(cups)
    removed = [cups.pop(1) for i in range(3)]
    print(removed)
    destination = cups[0] - 1
    while destination not in cups:
        destination -= 1
        if destination not in removed and destination not in cups:
            destination = max(max(cups), max(removed))
    print(destination)
    index = cups.index(destination)
    cups = cups[:index + 1] + removed + cups[index + 1:]
    cups = cups[1:] + [cups[0]]
    print(' ')
    return cups


def solve(data):
    for i in range(100):
        data = simulate(data)
    index = data.index(1)
    return ''.join([str(i) for i in data[index + 1:]]) + ''.join([str(i) for i in data[:index]])


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        data = []
        for c in lines[0]:
            data.append(int(c))
        return data


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
