def is_valid(row):
    c = row[3].count(row[2])
    return c >= row[0] and c <= row[1]

def solve(data):
    return sum([1 if is_valid(row) else 0 for row in data])


def read(filename):
    with open(filename, 'r') as f:
        data = []
        for l in f.readlines():
            sp = l.split(' ')
            ra = [int(s) for s in sp[0].split('-')]
            data.append([
                ra[0],
                ra[1],
                sp[1][:-1],
                sp[2].rstrip()
            ])
        return data

def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\nAnswer {}".format(main(f)))
