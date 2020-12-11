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
            return -1
        if j < 0 or j >= len(state[0]):
            return -1
        return state[i][j]
    def count(i, j):
        directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        s = 0
        for d in directions:
            p = (i + d[0], j + d[1])
            v = get(p)
            while v == 0:
                p = (p[0] + d[0], p[1] + d[1])
                v = get(p)
            if v == 2:
                s += 1            
        return s

    changes = 0
    update = []
    for i, line in enumerate(state):
        l = []
        for j, c in enumerate(line):
            if c == 1 and count(i, j) == 0:
                l.append(2)
                changes += 1
            elif c == 2 and count(i, j) >= 5:
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
