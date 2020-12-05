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


def seat_id(bp):
    print((bp, row(bp), col(bp), row(bp) * 8 + col(bp)))
    return row(bp) * 8 + col(bp)


def solve(data):
    return max([seat_id(bp) for bp in data])


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
