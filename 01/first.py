def solve(data):
    data.sort()
    for i in data:
        for j in data[::-1]:
            if i + j == 2020:
                return i * j
            elif i + j > 2020:
                continue


def read(filename):
    with open(filename, 'r') as f:
        return [int(l) for l in f.readlines()]


def main(filename):
    return solve(read(filename))


if __name__ == "__main__":
    import sys
    if (len(sys.argv) < 2):
        print('missing input parameter')
        exit()
    for f in sys.argv[1:]:
        print("\nAnswer {}".format(main(f)))
