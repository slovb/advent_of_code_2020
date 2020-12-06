def count(group):
    s = set()
    for l in group:
        for c in l:
            s.add(c)
    return len(s)


def solve(data):
    return sum([count(group) for group in data])


def read(filename):
    with open(filename, 'r') as f:
        data = []
        group = []
        for line in f.readlines():
            l = line.rstrip()
            if l == '':
                data.append(group)
                group = []
            else:
                group.append(l)
        data.append(group)
        return data


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\n{}".format(main(f)))
