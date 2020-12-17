def paint(state):
    minX, minY, minZ, maxX, maxY, maxZ = None, None, None, None, None, None
    for p in state:
        minX = p[0] if minX == None else min(minX, p[0])
        minY = p[1] if minY == None else min(minY, p[1])
        minZ = p[2] if minZ == None else min(minZ, p[2])
        maxX = p[0] if maxX == None else max(maxX, p[0])
        maxY = p[1] if maxY == None else max(maxY, p[1])
        maxZ = p[2] if maxZ == None else max(maxZ, p[2])
    for z in range(minZ, maxZ + 1):
        print('z={}'.format(z))
        for y in range(minY, maxY + 1):
            row = []
            for x in range(minX, maxX + 1):
                if (x, y, z) in state:
                    row.append('#')
                else:
                    row.append('.')
            print(''.join(row))                
        print(' ')


def count(p, state):
    c = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == 0 and dy == 0 and dz == 0:
                    continue
                if (p[0] + dx, p[1] + dy, p[2] + dz) in state:
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
                neighbors.add((p[0] + dx, p[1] + dy, p[2] + dz))


def solve(data):
    state, neighbors = data
    for i in range(6):
        print('after {} cycles: {}'.format(i, len(state)))
        paint(state)
        state, neighbors = simulate(state, neighbors)
    return len(state)


def read(filename):
    with open(filename, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        state = set()
        neighbors = set()
        z = 0
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    p = (x, y, z)
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
