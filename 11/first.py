def paint(state):
    def p_line(line):
        out = []
        for c in line:
            if c == 0:
                out.append('.')
            elif c == 1:
                out.append('L')
            else:
                out.append('#')
        return ''.join(out)
    print('\n'.join([p_line(line) for line in state]))
    print(' ')


def simulate(state):
    def get(p):
        i, j = p
        if i < 0 or i >= len(state):
            return 0
        if j < 0 or j >= len(state[0]):
            return 0
        return state[i][j] == 2
    def count(i, j):
        positions = [(i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]
        return sum([get(p) for p in positions])

    changes = 0
    update = []
    for i, line in enumerate(state):
        l = []
        for j, c in enumerate(line):
            if c == 1 and count(i, j) == 0:
                l.append(2)
                changes += 1
            elif c == 2 and count(i, j) >= 4:
                l.append(1)
                changes += 1
            else:
                l.append(c)
        update.append(l)
    return update, changes

def solve(data):
    def count(state):
        s = 0
        for line in state:
            for c in line:
                if c == 2:
                    s += 1
        return s
    paint(data)
    state, changes = simulate(data)
    while changes != 0:
        paint(state)
        state, changes = simulate(state)
    paint(state)
    return count(state)

def read(filename):
    with open(filename, 'r') as f:
        def process(line):
            data = []
            for c in line:
                if c == 'L':
                    data.append(1)
                else:
                    data.append(0)
            return data
        return [process(line.rstrip()) for line in f.readlines()]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print("\n{}".format(main('input.txt')))
    else:
        for f in sys.argv[1:]:
            print("\n{}".format(main(f)))
