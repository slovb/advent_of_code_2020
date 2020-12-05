def row(bp):
    v = 0
    s = 64
    for d in bp[:7]:
        if d == 'B':
            v += s
        s //= 2
    return v


def col(bp):
    v = 0
    s = 4
    for d in bp[7:]:
        if d == 'R':
            v += s
        s //= 2
    return v


def solve(data):
    positions = [(row(bp), col(bp)) for bp in data]
    min_pos = min(positions)
    max_pos = max(positions)
    for r in range(min_pos[0] + 1, max_pos[0]): # ignore the first and final row as they are messy
        for c in range(8):
            if (r, c) not in positions:
                return (r, c), r * 8 + c


def read(filename):
    with open(filename, 'r') as f:
        def process(line):
            return line.rstrip()
        return [process(l) for l in f.readlines()]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\n{}".format(main(f)))
