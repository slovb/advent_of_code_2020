def solve(data):
    p = 0
    count = 0
    for l in data:
        print('{} {} {}'.format(p, l[p%len(l)], l))
        if l[p%len(l)] == '#':
            count += 1
        p += 3
    return count


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
