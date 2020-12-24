def walk(instruction, x = 0, y = 0):
    for i in instruction:
        if i == 'e':
            x += 1
        elif i == 'w':
            x -= 1
        elif i == 'se':
            if y % 2 == 1:
                x += 1
            y += 1
        elif i == 'sw':
            if y % 2 == 0:
                x -= 1
            y += 1
        elif i == 'ne':
            if y % 2 == 1:
                x += 1
            y -= 1
        elif i == 'nw':
            if y % 2 == 0:
                x -= 1
            y -= 1
    return (x, y)


def solve(data):
    positions = {}
    for instruction in data:
        pos = walk(instruction)
        print(pos, instruction)
        if pos in positions:
            positions[pos] = not positions[pos]
        else:
            positions[pos] = True
    total = 0
    for pos in positions:
        if positions[pos]:
            total += 1
    return total


def read(filename):
    def process(line):
        instructions = []
        i = 0
        while i < len(line):
            c = line[i]
            if c in ['s', 'n']:
                i += 1
                c += line[i]
            instructions.append(c)
            i += 1
        return instructions
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        return [process(line) for line in lines]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
