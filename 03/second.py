def count(data, r, d):
    p = 0
    count = 0
    for l in data[::d]:
        if l[p%len(l)] == '#':
            count += 1
        p += r
    return count

def solve(data):
    prod = 1
    for r, d in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        prod *= count(data, r, d)
    return prod


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
        print("\nAnswer {}".format(main(f)))
