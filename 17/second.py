def count(p, state):
    c = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                        continue
                    if (p[0] + dx, p[1] + dy, p[2] + dz, p[3] + dw) in state:
                        c += 1
    return c


def simulate(state, neighbors):
    updated_state = set()
    updated_neighbors = set()
    for p in neighbors:
        c = count(p, state)
        if c == 3 or (c == 2 and p in state):
            updated_state.add(p)
            add_neighbors(p, updated_neighbors)
    return updated_state, updated_neighbors


def add_neighbors(p, neighbors):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    neighbors.add((p[0] + dx, p[1] + dy, p[2] + dz, p[3] + dw))


def solve(data):
    state, neighbors = data
    for i in range(6):
        print('after {} cycles: {}'.format(i, len(state)))
        #paint(state)
        state, neighbors = simulate(state, neighbors)
    return len(state)


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        state = set()
        neighbors = set()
        z = 0
        w = 0
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    p = (x, y, z, w)
                    add_neighbors(p, neighbors)
                    state.add(p)
        return (state, neighbors)


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
