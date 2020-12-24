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


def get_adjacent(p):
    x, y = p
    dir = ['e', 'w', 'se', 'sw', 'ne', 'nw']
    adjacent = []
    for d in dir:
        adjacent.append(walk([d], x, y))
    return adjacent


def count_adjacent(p, state):
    total = 0
    for a in get_adjacent(p):
        if a in state and state[a]:
            total += 1
    return total


def count(state):
    total = 0
    for p in state:
        if state[p]:
            total += 1
    return total


def initialize(instructions):
    state = {}
    notable = set()
    for instruction in instructions:
        pos = walk(instruction)
        if pos in state:
            state[pos] = not state[pos]
        else:
            state[pos] = True
            notable.add(pos)
            for a in get_adjacent(pos):
                notable.add(a)
    return state, notable


def simulate(state, notable):
    update = {}
    update_notable = set()
    for p in notable:
        if p in state and state[p]:
            c = count_adjacent(p, state)
            if c == 0 or c > 2:
                pass
            else:
                update[p] = True
                for a in get_adjacent(p):
                    update_notable.add(a)
        else:
            c = count_adjacent(p, state)
            if c == 2:
                update[p] = True
                for a in get_adjacent(p):
                    update_notable.add(a)
    return update, update_notable


def solve(data):
    state, notable = initialize(data)
    for i in range(100):
        state, notable = simulate(state, notable)
        print('Day {}: {}'.format(i + 1, count(state)))
    return count(state)


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
